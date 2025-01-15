import http.server
from prometheus_client import start_http_server, Counter

REQUESTS = Counter('test_requests_total', 'Total GET requests for our test server.')

class myHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


if __name__ == '__main__':
    start_http_server(5001)
    server = http.server.HTTPServer(('192.168.30.29', 5000), myHandler)
    server.serve_forever()
