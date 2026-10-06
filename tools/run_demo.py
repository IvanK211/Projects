#!/usr/bin/env python3
"""Exercise every offline CLI using only bundled synthetic data."""
import argparse,subprocess,sys,tempfile,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def run(output: Path):
    output.mkdir(parents=True,exist_ok=True)
    commands=[
      ['inventory','examples/inventory.json','inventory.json'],
      ['compare','examples/inventory-before.json','examples/inventory-after.json','comparison.json'],
      ['training','examples/training.json','training.json'],
      ['phishing','examples/phishing.json','phishing.json'],
      ['pim','examples/pim.json','pim.json','--since','2001-01-01T00:00:00Z'],
      ['pam-plan','examples/pam-accounts.json','plan.json','--suffix','example.invalid','--port','8443'],
      ['sessions','examples/pam-sessions.json','sessions.json'],
      ['plugins','examples/plugins.json','plugins.json'],
      ['risks','examples/risks.json','risks.json','--as-of','2001-04-01T00:00:00Z'],
      ['sensors','examples/sensors.json','sensors.json'],
      ['logs','examples/logs.json','logs.json'],
      ['correlate','examples/ip-observations.json','correlation.json','--ip','192.0.2.10','--as-of','2001-01-03T00:00:00Z'],
      ['kpis','examples/kpis.json','kpis.json'],
      ['fit','--source','80','50','24','--target','75','45','25','--clearance','0.25','fit.json'],
      ['energy','--voltage','5','--amp-hours','2','--watts','1','--usable-fraction','0.8','--efficiency','0.9','energy.json'],
      ['flow','--collected-liters','1','--seconds','20','--reservoir-liters','10','flow.json'],
      ['html','examples/kpis.json','report.html','--title','Synthetic reference report'],
    ]
    for args in commands:
        # Only the output argument is bare; inputs are rooted in examples/.
        args=[str(output/a) if (a.endswith('.json') or a.endswith('.html')) and '/' not in a else a for a in args]
        result=subprocess.run([sys.executable,'-m','labkit',*args],cwd=ROOT,capture_output=True,text=True,timeout=15)
        if result.returncode: raise RuntimeError(f'Demo failed: {args[0]} (exit {result.returncode})')
    for p in output.glob('*.json'):json.loads(p.read_text())
    print(f'{len(commands)} offline commands passed using synthetic fixtures.')
    return len(commands)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path)
    args=p.parse_args()
    if args.output: run(args.output.resolve())
    else:
        with tempfile.TemporaryDirectory(prefix='reference-demo-') as folder:run(Path(folder))
    return 0
if __name__=='__main__':sys.exit(main())
