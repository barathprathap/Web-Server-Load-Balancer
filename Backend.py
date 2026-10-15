import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


server_name = sys.argv[1]


class BackendHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"Response from {server_name}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


port = int(sys.argv[2])
server = HTTPServer(("localhost", port), BackendHandler)
print(f"{server_name} listening on port {port}")
server.serve_forever()