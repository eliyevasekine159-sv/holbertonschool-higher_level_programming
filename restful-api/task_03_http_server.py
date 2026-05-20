#!/usr/bin/python3
"""
A simple HTTP API server using Python's built-in http.server module.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    HTTP Request Handler that serves basic plain text and JSON endpoints.
    """

    def do_GET(self):
        """Handles GET requests for specific API endpoints"""

        # 1. Root Endpoint
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. Data Endpoint
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sample_data = {
                "name": "John Doe",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))

        # 3. Status Endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. Undefined / Səhv Endpoint-lər (Bayaq xəta verən və tapılmayan hissə)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Starts the HTTP server on specified port"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
