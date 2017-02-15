from html.parser import HTMLParser

class HeadingParser(HTMLParser):
	inHeading = False

	# 遇到一个标签时调用
	def handle_starttag(self, tag, attrs): 
		if tag == "h1":
			self.inHeading = True
			print("Found a Heading 1")

	# 遇到文本数据时调用
	def handle_data(self, data):
		if self.inHeading:
			print(data)

	def handle_endtag(self, tag):
		if tag == "h1":
			self.inHeading = False

hParser = HeadingParser()
file = open("test.html", "r")
html = file.read()
file.close()

hParser.feed(html)