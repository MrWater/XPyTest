#! /usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

host = '192.168.1.105'
port = 8888
buffer_size = 1024
addr = (host, port)

conn_sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
conn_sock.bind(addr)

print('waiting for client...')

data = conn_sock.recvfrom(buffer_size)

if data is not None:
	print('client: ', data[0])

conn_sock.close()
