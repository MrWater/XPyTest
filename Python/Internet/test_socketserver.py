import socketserver

class RequestHandler(socketserver.StreamRequestHandler):
	"""Handlers one request to mirror som text."""

	def handle(self):
		l = True
		while l:
			l = self.rfile.readline().strip()

			if l:
				self.wfile.write(l[::-1] + bytes("\n", "utf-8"))

if __name__ == "__main__":