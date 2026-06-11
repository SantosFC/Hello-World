import socket
import urllib.request
from http.server import BaseHTTPRequestHandler

PING_URL = "https://hc-ping.com/4f9a5abf-38d6-4f34-a698-9e97c3a62632"


def do_ping():
    try:
        urllib.request.urlopen(PING_URL, timeout=10)
        return {"status": "ok", "message": "Ping sent successfully"}
    except socket.error as e:
        return {"status": "error", "message": f"Ping failed: {e}"}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        result = do_ping()
        body = str(result).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        import json
        self.wfile.write(json.dumps(result).encode())
