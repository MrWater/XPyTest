from xml.dom.minidom import parse
import xml.dom.minidom

try:
	html = parse("test.html")
	body = html.getElementsByTagName("body")
	ele = html.createElement("h2")
	node = html.createTextNode("fsfsdf")
	ele.appendChild(node)
	body[0].appendChild(ele)

	file = open("test.xml", "w", encoding="utf-8")
	file.write(html.toxml())
	file.close()
except Exception as e:
	print("错误" + e)

   