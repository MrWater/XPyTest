import http.server
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

def run(server_class = HTTPServer, handler_class = CGIHTTPRequestHandler):
	server_address = ("localhost", 8001)
	httpd = server_class(server_address, handler_class)
	httpd.serve_forever()

if __name__ == '__main__':
	run()