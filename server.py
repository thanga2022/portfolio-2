import http.server
import socketserver
import os

PORT = 5000

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"{self.address_string()} - [{self.log_date_time_string()}] {format % args}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("0.0.0.0", PORT), NoCacheHTTPRequestHandler) as httpd:
    print(f"Server running at http://0.0.0.0:{PORT}/")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever()
