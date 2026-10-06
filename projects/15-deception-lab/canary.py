#!/usr/bin/env python3
"""Local demonstration only: no fake login form, credential collection or command execution."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, timezone
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Do not record query strings, client addresses, headers, or request bodies.
        print(json.dumps({'eventType':'decoyInteraction','time':datetime.now(timezone.utc).isoformat(),
                          'method':'GET','source':'local-reference'}),flush=True)
        self.send_response(404)
        self.send_header('Content-Type','text/plain; charset=utf-8')
        self.send_header('Content-Security-Policy',"default-src 'none'")
        self.end_headers()
        self.wfile.write(b'Reference endpoint\n')
    def log_message(self,fmt,*args):
        return
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--port',type=int,default=8098)
    a=p.parse_args()
    if not 1 <= a.port <= 65535: p.error('Invalid port')
    try:
        HTTPServer(('127.0.0.1',a.port),Handler).serve_forever()
    except KeyboardInterrupt:
        pass
