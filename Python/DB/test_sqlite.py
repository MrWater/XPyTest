import os
import sqlite3

conn = sqlite3.connect("db.ttfb")
cursor = conn.cursor()
cursor.execute("drop table if exists test");
cursor.execute("""
	create table test(
		id integer primary key autoincrement,
		name varchar(256))
	""");
cursor.executemany("insert into test(name) values(?)", [("1"),("2"),("3"),("4")])
conn.commit()
cursor.close()
conn.close()