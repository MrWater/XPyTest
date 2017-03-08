# !/user/bin/env python

import time

from socket import *


host = ''
port = 21567
buffer_size = 1024
addr = (host, port)

tcp_server_sock = socket(AF_INET, SOCK_STREAM)
tcp_server_sock.bind(addr)
tcp_server_sock.listen(5)

while True:
	print('waiting for connection')
	tcp_client_sock, addr = tcp_server_sock.accept()
	print('...connected from:', addr)

	
	data = tcp_client_sock.recv(buffer_size)

	if not data:
		break

	tcp_client_sock.send(bytes('[%s] %s' % (time.ctime(), data), encoding='utf8'))

	tcp_client_sock.close()

tcp_server_sock.close()
