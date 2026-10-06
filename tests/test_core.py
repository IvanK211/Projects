"""Regression tests use synthetic data and never authenticate or query a network."""
from __future__ import annotations
import copy,json,math,os,subprocess,sys,tempfile,unittest
from pathlib import Path
from labkit import common,inventory,awareness,pam,telemetry,vulnerability,engineering,reporting,endpoints
ROOT=Path(__file__).resolve().parents[1]
def fixture(name):return json.loads((ROOT/'examples'/name).read_text())
T='2001-01-01T00:00:00Z'

class CommonTests(unittest.TestCase):
    def test_timestamp_utc(self):self.assertEqual(common.timestamp(T).utcoffset().total_seconds(),0)
    def test_timestamp_offset(self):self.assertEqual(common.timestamp(T),common.timestamp('2001-01-01T02:00:00+02:00'))
    def test_timestamp_missing(self):self.assertIsNone(common.timestamp(None))
    def test_timestamp_naive(self):
        with self.assertRaises(ValueError):common.timestamp('2001-01-01T00:00:00')
    def test_zero_denominator(self):self.assertIsNone(common.ratio(0,0))
    def test_fraction(self):self.assertEqual(common.ratio(1,4),.25)
    def test_count_negative(self):
        with self.assertRaises(ValueError):common.count(-1,'count')
    def test_count_noninteger(self):
        with self.assertRaises(ValueError):common.count(1.2,'count')
    def test_count_bool(self):
        with self.assertRaises(ValueError):common.count(True,'count')
    def test_nonfinite(self):
        for v in [float('nan'),float('inf')]:
            with self.subTest(value=str(v)),self.assertRaises(ValueError):common.number(v,'value')
    def test_private_roundtrip(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'value.json';common.write_json(p,{'value':1});self.assertEqual(common.load_json(p),{'value':1})
            if os.name=='posix':self.assertEqual(p.stat().st_mode&0o777,0o600)
    def test_private_text_roundtrip(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'report.html';common.write_text_private(p,'<p>Synthetic</p>')
            self.assertEqual(p.read_text(),'<p>Synthetic</p>')
            if os.name=='posix':self.assertEqual(p.stat().st_mode&0o777,0o600)
    def test_atomic_invalid_value_preserves_original(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'value.json';common.write_json(p,{'value':1})
            with self.assertRaises(ValueError):common.write_json(p,{'value':float('nan')})
            self.assertEqual(common.load_json(p),{'value':1})
            self.assertEqual(len(list(Path(folder).iterdir())),1)

class InventoryTests(unittest.TestCase):
    def setUp(self):self.row={'id':'d-a','deviceName':'LAB-A','lastSyncDateTime':T}
    def test_exact_case_match(self):self.assertEqual(inventory.reconcile(['lab-a'],[self.row])[0]['status'],'Found')
    def test_substring_does_not_match(self):self.assertEqual(inventory.reconcile(['lab'],[self.row])[0]['status'],'NotFound')
    def test_request_duplicate_collapsed(self):self.assertEqual(len(inventory.reconcile(['lab-a',' LAB-A '],[self.row])),1)
    def test_record_duplicate_rejected(self):
        with self.assertRaises(ValueError):inventory.reconcile(['LAB-A'],[self.row,self.row])
    def test_duplicate_newest_oldest(self):
        older={**self.row,'id':'d-b','lastSyncDateTime':None}
        result=inventory.reconcile(['LAB-A'],[self.row,older])[0]
        self.assertEqual(result['status'],'Duplicate');self.assertEqual(result['newest']['id'],'d-a');self.assertEqual(result['oldest']['id'],'d-b')
    def test_timestamp_tie_breaker(self):
        result=inventory.reconcile(['LAB-A'],[self.row,{**self.row,'id':'d-z'}])[0]
        self.assertEqual(result['newest']['id'],'d-z')
    def test_empty_name_record(self):
        with self.assertRaises(ValueError):inventory.reconcile([],[{**self.row,'deviceName':''}])
    def test_compare_all_states(self):
        old=[{'id':'a','v':1},{'id':'b'},{'id':'c'}];new=[{'id':'a','v':2},{'id':'c'},{'id':'d'}]
        r=inventory.compare(old,new);self.assertEqual(len(r['changed']),1);self.assertEqual(r['added'][0]['id'],'d');self.assertEqual(r['removed'][0]['id'],'b');self.assertEqual(r['unchangedCount'],1)
    def test_compare_duplicate(self):
        with self.assertRaises(ValueError):inventory.compare([{'id':'a'},{'id':'A'}],[])

class TrainingTests(unittest.TestCase):
    def test_known_totals(self):
        r=awareness.training_audit(fixture('training.json'))['groups'];a=r['Group Alpha'];b=r['Group Beta']
        self.assertEqual((a['expected'],a['completed'],a['incomplete'],a['notAssigned']),(4,2,1,1))
        self.assertEqual((b['expected'],b['notAssigned']),(2,2))
    def test_inactive_excluded(self):
        d=fixture('training.json');d['users'][0]['active']=False
        self.assertEqual(awareness.training_audit(d)['groups']['Group Alpha']['expected'],2)
    def test_duplicate_users_rejected(self):
        d=fixture('training.json');d['users'].append(d['users'][0])
        with self.assertRaises(ValueError):awareness.training_audit(d)
    def test_duplicate_requirements_rejected(self):
        d=fixture('training.json');d['requiredTrainingIds']=['a',' A ']
        with self.assertRaises(ValueError):awareness.training_audit(d)
    def test_zero_obligations_unknown_rate(self):
        d=fixture('training.json');d['requiredTrainingIds']=[]
        self.assertIsNone(awareness.training_audit(d)['groups']['Group Alpha']['completionRate'])
    def test_completion_not_double_counted(self):
        d=fixture('training.json');d['enrollments'].append(copy.deepcopy(d['enrollments'][0]))
        self.assertEqual(awareness.training_audit(d)['groups']['Group Alpha']['completed'],2)

class PhishingTests(unittest.TestCase):
    def sample(self):return [{'campaignId':'a','division':'g','delivered':40,'failed':4},{'campaignId':'b','division':'g','delivered':80,'failed':2}]
    def test_weighting(self):
        r=awareness.phishing_summary(self.sample())[0];self.assertEqual(r['recipientExposureWeightedFailureRate'],.05);self.assertEqual(r['campaignMeanFailureRate'],.0625)
    def test_zero_deliveries(self):
        r=awareness.phishing_summary([{'campaignId':'a','division':'g','delivered':0,'failed':0}])[0]
        self.assertIsNone(r['reportRate']);self.assertIsNone(r['campaignMeanFailureRate'])
    def test_overcount_rejected(self):
        row=self.sample()[0];row['failed']=41
        with self.assertRaises(ValueError):awareness.phishing_summary([row])
    def test_duplicate_campaign_rejected(self):
        row=self.sample()[0]
        with self.assertRaises(ValueError):awareness.phishing_summary([row,row])
    def test_negative_count_rejected(self):
        row=self.sample()[0];row['delivered']=-1
        with self.assertRaises(ValueError):awareness.phishing_summary([row])

class PimTests(unittest.TestCase):
    def test_status_retained(self):
        rows=[{'id':'a','action':'selfActivate','status':'Denied','createdDateTime':T}]
        self.assertEqual(awareness.pim_activations(rows,T)[0]['status'],'Denied')
    def test_other_action_excluded(self):self.assertEqual(awareness.pim_activations([{'action':'adminAssign','createdDateTime':T}],T),[])
    def test_cutoff_inclusive(self):self.assertEqual(len(awareness.pim_activations([{'id':'a','action':'selfActivate','createdDateTime':T}],T)),1)
    def test_offset_order(self):
        rows=[{'id':'later','action':'selfActivate','createdDateTime':'2001-01-01T01:00:00Z'},
              {'id':'earlier','action':'selfActivate','createdDateTime':'2001-01-01T02:00:00+02:00'}]
        self.assertEqual([r['id'] for r in awareness.pim_activations(rows,T)],['earlier','later'])

class PamTests(unittest.TestCase):
    def sample(self):return {'id':'a','address':'app.example.invalid','safeName':'lab-safe','platformId':'platform-a','platformAccountProperties':{'Port':'22','Other':'keep'}}
    def test_label_boundary(self):
        a=self.sample();b={**a,'id':'b','address':'notexample.invalid'}
        self.assertEqual(len(pam.port_plan([a,b],'example.invalid',8443)['accounts']),1)
    def test_other_properties_preserved(self):
        a=self.sample();r=pam.port_plan([a],'example.invalid',8443)['accounts'][0]
        self.assertEqual(r['afterProperties']['Other'],'keep');self.assertEqual(a['platformAccountProperties']['Port'],'22')
        self.assertIsInstance(r['patch'],list);self.assertEqual(r['patch'][0]['value']['Port'],'8443')
    def test_port_range(self):
        for value in [0,65536,-1]:
            with self.subTest(port=value),self.assertRaises(ValueError):pam.port_plan([self.sample()],'example.invalid',value)
    def test_safe_scope(self):self.assertEqual(pam.port_plan([self.sample()],'example.invalid',8443,'other-safe')['accounts'],[])
    def test_port_casing_ambiguous(self):
        a=self.sample();a['platformAccountProperties']['port']='22'
        with self.assertRaises(ValueError):pam.port_plan([a],'example.invalid',8443)
    def test_unchanged(self):self.assertEqual(pam.port_plan([self.sample()],'example.invalid',22)['accounts'][0]['action'],'unchanged')
    def test_malformed_suffix(self):
        for value in ['*','invalid','example..invalid','-bad.invalid']:
            with self.subTest(suffix=value),self.assertRaises(ValueError):pam.normalize_suffix(value)
    def test_duplicate_account(self):
        a=self.sample()
        with self.assertRaises(ValueError):pam.port_plan([a,a],'example.invalid',8443)
    def test_session_initiator_and_missing_duration(self):
        rows=[{'id':'a','initiatingUser':'person-a','targetUser':'root','start':T,'end':'2001-01-01T00:01:00Z'},
              {'id':'b','initiatingUser':'person-a','targetUser':'admin','start':T,'end':None}]
        r=pam.session_summary(rows)[0];self.assertEqual((r['initiatingUser'],r['sessions'],r['knownDurationSeconds'],r['unknownDuration']),('person-a',2,60,1))
    def test_negative_session_duration(self):
        with self.assertRaises(ValueError):pam.session_summary([{'id':'a','start':'2001-01-02T00:00:00Z','end':T}])

class TelemetryTests(unittest.TestCase):
    def previous(self):return {'count':100,'time':T,'source':'a'}
    def current(self):return {'count':120,'time':'2001-01-01T00:00:10Z','source':'a'}
    def test_rate(self):self.assertEqual(telemetry.counter_rate(self.previous(),self.current()),2)
    def test_first_rate_unknown(self):self.assertIsNone(telemetry.counter_rate(None,self.current()))
    def test_reset_rate_unknown(self):self.assertIsNone(telemetry.counter_rate(self.previous(),{**self.current(),'count':1}))
    def test_source_changed_unknown(self):self.assertIsNone(telemetry.counter_rate(self.previous(),{**self.current(),'source':'b'}))
    def test_time_reversal_unknown(self):self.assertIsNone(telemetry.counter_rate(self.current(),self.previous()))
    def test_sensor_units_separate(self):
        rows=[{'sensor':'s','unit':'C','value':20,'time':T},{'sensor':'s','unit':'mV','value':100,'time':T}]
        self.assertEqual(len(telemetry.sensor_summary(rows)['series']),2)
    def test_sensor_drift(self):
        rows=[{'sensor':'s','unit':'C','value':20,'time':T},{'sensor':'s','unit':'C','value':22,'time':'2001-01-01T02:00:00Z'}]
        r=telemetry.sensor_summary(rows)['series'][0];self.assertEqual(r['endpointDriftPerHour'],1);self.assertEqual(r['median'],21)
    def test_nonfinite_sensor_rejected(self):
        with self.assertRaises(ValueError):telemetry.sensor_summary([{'sensor':'s','unit':'C','value':math.inf,'time':T}])
    def test_log_messages_absent(self):
        r=telemetry.log_summary([{'level':'INFO','eventType':'demo','message':'PRIVATE-MESSAGE-SAMPLE','user':'sample-person'}])
        self.assertNotIn('PRIVATE-MESSAGE-SAMPLE',json.dumps(r));self.assertNotIn('sample-person',json.dumps(r))
    def test_ip_stale_and_multiple(self):
        rows=[{'ip':'192.0.2.10','time':T,'device':'a'},{'ip':'192.0.2.10','time':'2001-01-03T00:00:00Z','device':'b'}]
        r=telemetry.correlate_ip(rows,'192.0.2.10','2001-01-03T01:00:00Z',12)['observations']
        self.assertEqual(len(r),2);self.assertTrue(r[0]['stale']);self.assertFalse(r[1]['stale'])
    def test_ip_future_flag(self):
        r=telemetry.correlate_ip([{'ip':'192.0.2.10','time':'2001-01-02T00:00:00Z'}],'192.0.2.10',T,12)
        self.assertTrue(r['observations'][0]['futureDated'])

class VulnerabilityTests(unittest.TestCase):
    def test_metadata_not_numeric_id(self):
        rows=[{'pluginId':'demo-a','name':'Debian package advisory'},{'pluginId':'demo-b','family':'VMware ESXi'}]
        r=vulnerability.classify_plugins(rows);self.assertEqual(r[0]['classifications'],['Debian']);self.assertEqual(r[1]['classifications'],['VMware ESXi'])
    def test_unknown_stays_unknown(self):self.assertEqual(vulnerability.classify_plugins([{'pluginId':'demo'}])[0]['classifications'],['OtherOrUnknown'])
    def test_rule_id_not_plugin(self):
        with self.assertRaises(ValueError):vulnerability.classify_plugins([{'ruleId':'rule-a'}])
    def test_risk_expired(self):self.assertEqual(vulnerability.review_risks([{'expires':T}],T)[0]['status'],'expired')
    def test_missing_evidence_independent(self):
        r=vulnerability.review_risks([{'expires':'2001-02-01T00:00:00Z'}],T)[0]
        self.assertEqual(r['status'],'current');self.assertIn('owner',r['missingEvidenceFields'])

class EngineeringTests(unittest.TestCase):
    def test_uniform_fit(self):
        r=engineering.fit_scale([10,20,30],[20,20,30]);self.assertEqual(r['uniformScale'],1)
    def test_clearance_per_side(self):self.assertEqual(engineering.fit_scale([10,10,10],[12,12,12],1)['uniformScale'],1)
    def test_clearance_reject(self):
        with self.assertRaises(ValueError):engineering.fit_scale([1,1,1],[1,1,1],1)
    def test_energy(self):self.assertAlmostEqual(engineering.energy_budget(5,2,1,.8,.9)['estimatedHours'],7.2)
    def test_efficiency_invalid(self):
        with self.assertRaises(ValueError):engineering.energy_budget(5,2,1,.8,1.1)
    def test_flow(self):
        r=engineering.flow_measurement(1,20,12);self.assertEqual(r['measuredLitersPerMinute'],3);self.assertEqual(r['idealVolumeTurnoverMinutes'],4)
    def test_zero_flow_time(self):
        with self.assertRaises(ValueError):engineering.flow_measurement(1,0,12)

class ReportTests(unittest.TestCase):
    def test_html_escaped(self):
        r=reporting.html_report({'value':'<script>alert(1)</script>'},'<b>demo</b>')
        self.assertNotIn('<script>',r);self.assertIn('&lt;script&gt;',r);self.assertIn('&lt;b&gt;demo&lt;/b&gt;',r)
    def test_kpi_empty(self):self.assertIsNone(reporting.kpi_summary([{'name':'demo','kind':'mean','values':[]}])['metrics'][0]['value'])
    def test_kpi_aggregations(self):
        r=reporting.kpi_summary([{'name':kind,'kind':kind,'values':[1,3]} for kind in ['sum','mean','last']])
        self.assertEqual([m['value'] for m in r['metrics']],[4,2,3])
    def test_unknown_aggregation(self):
        with self.assertRaises(ValueError):reporting.kpi_summary([{'name':'demo','kind':'guess','values':[1]}])

class EndpointTests(unittest.TestCase):
    def test_exact_host(self):
        text='https://old.example.invalid/api?q=1 https://other.example.invalid/api'
        out,changes=endpoints.propose_replacements(text,{'old.example.invalid':'new.example.invalid'})
        self.assertEqual(out,'https://new.example.invalid/api?q=1 https://other.example.invalid/api');self.assertEqual(len(changes),1)
    def test_port_preserved(self):
        out,_=endpoints.propose_replacements('https://old.example.invalid:8443/api',{'old.example.invalid':'new.example.invalid'})
        self.assertEqual(out,'https://new.example.invalid:8443/api')
    def test_credentials_rejected(self):
        source='https'+'://'+'user'+':'+'not-a-real-secret'+'@'+'old.example.invalid/api'
        with self.assertRaises(ValueError):endpoints.propose_replacements(source,{})
    def test_map_rejects_url(self):
        with self.assertRaises(ValueError):endpoints.propose_replacements('',{'a.example.invalid':'https://b.example.invalid'})

class CliTests(unittest.TestCase):
    def test_refuses_input_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'input.json';common.write_json(p,[]);original=p.read_bytes()
            result=subprocess.run([sys.executable,'-m','labkit','logs',str(p),str(p)],cwd=ROOT,capture_output=True)
            self.assertEqual(result.returncode,2);self.assertEqual(p.read_bytes(),original)
    def test_error_does_not_echo_input(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'input.json';p.write_text('{DO-NOT-PRINT-THIS-SYNTHETIC-ERROR')
            result=subprocess.run([sys.executable,'-m','labkit','logs',str(p),str(Path(folder)/'out.json')],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,2);self.assertNotIn('DO-NOT-PRINT',result.stderr)
    def test_cli_help(self):
        result=subprocess.run([sys.executable,'-m','labkit','--help'],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,0);self.assertIn('pam-plan',result.stdout)

if __name__=='__main__':unittest.main()
