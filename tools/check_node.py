#!/usr/bin/env python3
"""Optional local HTTP checks for the snapshot viewer. Needs Node and Python.

Only an ephemeral loopback listener and temporary synthetic snapshots are used.
No credentials or external network services are contacted.
"""
import http.client,json,os,shutil,socket,subprocess,tempfile,time
from datetime import datetime,timezone,timedelta
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    node=shutil.which('node')
    if not node:raise SystemExit('Node is required for this optional runtime check.')
    source=ROOT/'projects/13-siem-health-dashboard/server.mjs'
    subprocess.run([node,'--check',str(source)],check=True)
    with tempfile.TemporaryDirectory(prefix='snapshot-test-') as folder:
        fixture=Path(folder)/'snapshot.json'
        fixture.write_text((ROOT/'examples/siem-health.json').read_text())
        with socket.socket() as sock:
            sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
        env={**os.environ,'PORT':str(port),'SNAPSHOT_FILE':str(fixture)}
        process=subprocess.Popen([node,str(source)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
        checks=0
        def request(path,method='GET'):
            conn=http.client.HTTPConnection('127.0.0.1',port,timeout=3)
            try:
                conn.request(method,path);res=conn.getresponse()
                return res.status,dict(res.getheaders()),res.read().decode()
            finally:conn.close()
        def expect(condition):
            nonlocal checks
            if not condition:raise AssertionError('Snapshot runtime check failed')
            checks+=1
        def write(states,offset=0):
            fixture.write_text(json.dumps({'observedAt':(datetime.now(timezone.utc)+timedelta(seconds=offset)).isoformat(),
                                          'subsystems':[{'name':'fictional','state':s} for s in states]}))
        try:
            for _ in range(60):
                try:status,headers,body=request('/healthz');break
                except OSError:
                    if process.poll() is not None:raise RuntimeError('Viewer failed to start')
                    time.sleep(.05)
            else:raise RuntimeError('Viewer startup timeout')
            expect(status==200 and json.loads(body)['ok'] is True)
            status,headers,body=request('/readyz');expect(status==503 and json.loads(body)['overall']=='unknown')
            write([]);status,_,body=request('/readyz');expect(status==503 and json.loads(body)['overall']=='unknown')
            write(['healthy']);status,_,body=request('/readyz');expect(status==200 and json.loads(body)['overall']=='healthy')
            write(['failed']);status,_,body=request('/readyz');expect(status==503 and json.loads(body)['overall']=='failed')
            write(['healthy'],600);status,_,body=request('/readyz');expect(status==503 and json.loads(body)['overall']=='unknown')
            fixture.write_text('{invalid');status,_,body=request('/api/health');expect(status==503 and 'invalid' in json.loads(body)['error'])
            status,headers,body=request('/');expect(status==200 and 'Content-Security-Policy' in headers)
            status,_,body=request('/app.js');expect(status==200 and '.textContent=' in body and '.innerHTML' not in body)
            status,_,_=request('/missing');expect(status==404)
            status,_,_=request('/healthz','POST');expect(status==405)
        finally:
            process.terminate()
            try:process.wait(timeout=5)
            except subprocess.TimeoutExpired:process.kill();process.wait(timeout=5)
            if process.stderr:process.stderr.close()
    print(f'{checks} local Node HTTP checks passed; temporary listener and fixtures removed.')
if __name__=='__main__':main()
