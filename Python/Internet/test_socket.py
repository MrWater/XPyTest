import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("localhost", 8088))
sock.listen(1)

print("Wainting for a request.")

while 1:
	request, clientAddress = sock.accept()
	print("Received from", clientAddress, ":")
	print(type(request))
	data = request.recv(1024)
	print(data)
	request.shutdown(2)
sock.close()