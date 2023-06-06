"""
This file servers the local _output folder with the generated HTML files
for JupyterLite. This allows you to test the generated files locally, 
without having to deploy them to Github Pages.
"""

import http.server
import socketserver
import sys

PORT = 8000
DIRECTORY = "_output"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        print(f"Server running at localhost:{PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, shutting down the server...")
        httpd.shutdown()
        sys.exit(0)
