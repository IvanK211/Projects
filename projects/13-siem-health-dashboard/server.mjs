// Dependency-free, local-only synthetic/snapshot viewer. Not a live Wazuh connector.
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const file=process.env.SNAPSHOT_FILE || path.resolve(here,'../../examples/siem-health.json');
const port=Number(process.env.PORT || 8099);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('Invalid PORT');
function snapshot() {
  const stat=fs.statSync(file);
  if(stat.size > 2*1024*1024) throw new Error('Snapshot exceeds size limit');
  const data=JSON.parse(fs.readFileSync(file,'utf8'));
  if(!Array.isArray(data.subsystems)) throw new Error('Invalid snapshot');
  const observed=Date.parse(data.observedAt);
  if(!Number.isFinite(observed)) throw new Error('Missing timestamp');
  const age=Math.floor((Date.now()-observed)/1000);
  const stale=age>300 || age<0;
  const states=data.subsystems.map(s=>s.state);
  const overall=(stale || states.length===0)?'unknown':states.includes('failed')?'failed':states.includes('unknown')?'unknown':states.includes('degraded')?'degraded':states.every(s=>s==='healthy')?'healthy':'unknown';
  return {...data,ageSeconds:age,stale,overall};
}
const page=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>SIEM Health Reference</title></head><body><h1>SIEM Health Reference</h1><p>Snapshot viewer, not a production monitoring service. The bundled data is synthetic and deliberately historical.</p><pre id="result">Loading...</pre><script src="/app.js"></script></body></html>`;
const app=`async function refresh(){try{const response=await fetch('/api/health',{cache:'no-store'});const data=await response.json();document.getElementById('result').textContent=JSON.stringify(data,null,2);}catch(e){document.getElementById('result').textContent='Snapshot unavailable';}}refresh();setInterval(refresh,15000);`;
const server=http.createServer((req,res)=>{
  res.setHeader('Content-Security-Policy',"default-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'");
  res.setHeader('X-Content-Type-Options','nosniff');
  res.setHeader('Cache-Control','no-store');
  if(req.method!=='GET'){res.writeHead(405);return res.end();}
  let pathname;
  try {pathname=new URL(req.url,'http://localhost').pathname;}
  catch {res.writeHead(400);return res.end();}
  if(pathname==='/'){res.setHeader('Content-Type','text/html; charset=utf-8');return res.end(page);}
  if(pathname==='/app.js'){res.setHeader('Content-Type','application/javascript');return res.end(app);}
  res.setHeader('Content-Type','application/json');
  if(pathname==='/healthz') return res.end(JSON.stringify({ok:true,meaning:'Process liveness only'}));
  if(pathname==='/api/health' || pathname==='/readyz'){
    try{
      const state=snapshot();
      res.statusCode=pathname==='/readyz' && state.overall!=='healthy'?503:200;
      return res.end(JSON.stringify(state));
    }catch(e){res.statusCode=503;return res.end(JSON.stringify({overall:'unknown',error:'Snapshot unavailable or invalid'}));}
  }
  res.statusCode=404;res.end(JSON.stringify({error:'Not found'}));
});
server.requestTimeout=5000;server.headersTimeout=5000;
server.listen(port,'127.0.0.1',()=>console.log('Local reference viewer started. Keep snapshots private.'));
process.on('SIGTERM',()=>server.close());
