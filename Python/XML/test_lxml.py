import io
import lxml
from lxml import etree

html = open("test.xml", encoding="utf-8").read()
newsentence = io.StringIO(html)
info = etree.parse(newsentence)
print(etree.tostring(info))