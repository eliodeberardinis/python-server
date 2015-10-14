﻿
# code reduced from https://wiki.python.org/moin/BaseHttpServer

import time
import BaseHTTPServer

# example of a python class
 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):
    """Respond to a GET request."""
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write("<html><head><title>Title goes here.</title></head>")
    s.wfile.write("<body><p>This is a test.</p>")
    s.wfile.write("<p>You accessed path: %s</p>" % s.path)
    s.wfile.write("</body></html>")


httpd = BaseHTTPServer.HTTPServer(("172.31.31.13", 8000), MyHandler)
httpd.serve_forever()

