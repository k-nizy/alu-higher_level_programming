from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check for the custom header
        if self.headers.get("X-HolbertonSchool-User-Id") == "98":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"NOP")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 5001)  # Changed to port 5001
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
