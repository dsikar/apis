import sqlite3
# check we have all data imported
# connect
conn=sqlite3.connect('hackaday.db')
cur = conn.cursor()
# menus
cur.execute("SELECT COUNT(*) FROM tblProjects")
rows = cur.fetchall()
for row in rows:
	strPrint = str(row[0]);
print("Total rows in tblProjects = " + strPrint)
# todo
# number of records
# top instructions
# top skulls
# top followers
# fwd thinking
# most critical mass build
# top followers
cur.execute("SELECT * FROM tblProjects ORDER BY followers DESC LIMIT 1")
rows = cur.fetchall()
for row in rows:
	strPrint = str(row[2])
	print(strPrint)
# skulls
cur.execute("SELECT * FROM tblProjects ORDER BY skulls DESC LIMIT 1")
rows = cur.fetchall()
for row in rows:
	strPrint = str(row[2])
	print(strPrint)
# close connection
conn.close()
