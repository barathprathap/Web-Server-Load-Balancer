from itertools import cycle
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from http.server import BaseHTTPRequestHandler, HTTPServer


backends = cycle([
    "http://localhost:9001",
    "http://localhost:9002",
])


class BalancerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        backend = next(backends)
        target_url = backend + self.path
        request = Request(target_url, headers={"User-Agent": "PythonLoadBalancer"})

        try:
            response = urlopen(request, timeout=5)
        except HTTPError as error:
            response = error
        except URLError:
            self.send_error(502, "Backend server could not be reached")
            return

        body = response.read()
        self.send_response(response.status)
        self.send_header("Content-Type", response.headers.get("Content-Type", "text/plain"))
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer(("localhost", 8080), BalancerHandler)
print("Load balancer listening on http://localhost:8080")
server.serve_forever()
