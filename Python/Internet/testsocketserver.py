# !/user/bin/env python

from socketserver import TCPServer as TCP
from socketserver import StreamRequestHandler as SRH
from time import ctime

host = ''
port = 21567
addr = (host, port)

class MyRequestHandler(SRH):
	def handle(self):
		print('...connected from:', self.client_address)

tcp_server = TCP(addr, MyRequestHandler)
print('waiting for connection')
tcp_server.serve_forever()