import sqlite3
# check we have all data imported
# connect
conn=sqlite3.connect('hackaday.db')
cur = conn.cursor()
# menus
cur.execute("SELECT * FROM tblProjects")
rows = cur.fetchall()
for row in rows:
	strPrint = str(row[0]) + ", " + str(row[1]) + ", " + row[2] + ", " + row[3] + ", " + str(row[4])
	print(strPrint)
# todo
# number of records
# top instructions
# top skulls
# top followers
# fwd thinking
# most critical mass build
# top followers
cur.execute("SELECT * FROM tblProjects ORDER BY followers DESC LIMIT 1")
for row in rows:
	strPrint = str(row[0])
	print(strPrint)
# close connection
conn.close()
