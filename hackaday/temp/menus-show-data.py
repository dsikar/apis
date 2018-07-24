import sqlite3
# check we have all data imported
# connect
conn=sqlite3.connect('fireclass.db')
cur = conn.cursor()
# menus
cur.execute("SELECT * FROM tblMenus")
rows = cur.fetchall()
for row in rows:
	print(row[0])
# close connection
conn.close()
