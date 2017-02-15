import dbm

db = dbm.open("websites", "c")

db["www.python.org"] = "python home page"

value = db["www.python.org"]
if value != None:
	print(value)

db.close()