import sqlite3
# check we have all data imported
# connect
conn=sqlite3.connect('fireclass.db')
cur = conn.cursor()
# pages
cur.execute("SELECT * FROM tblPages")
rows = cur.fetchall()
for row in rows:
	print(row[0] + ", " + row[1])
# close connection
conn.close()
