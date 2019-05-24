import sqlite3

def encPrint(strPrint):
    # for strings with unprintable encoding
    # return strPrint.encode('ascii', 'ignore')
    # integers converted to strings, no problem
    return strPrint

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
# strSQL = 'CREATE TABLE \'tblProjects\' (\'id\' INTEGER, \'owner_id\' INTEGER, \'name\' TEXT, \'summary\' TEXT, \'views\' INTEGER, \'skulls\' INTEGER, \'followers\' INTEGER, \'logs\' INTEGER, \'details\' INTEGER, \'instruction\' INTEGER, \'created\' INTEGER, \'updated\' INTEGER);' # PRIMARY KEY NOT NULL);

print("Top 10 by followers")

cur.execute("SELECT id, name, followers FROM tblProjects ORDER BY followers DESC LIMIT 10")
rows = cur.fetchall()
for row in rows:
	strPrint = str(row[1])
	print(encPrint(strPrint))
# skulls
print("skulls")
cur.execute("SELECT id, name, skulls FROM tblProjects ORDER BY skulls DESC LIMIT 10")
rows = cur.fetchall()
for row in rows:
	strPrint = str(row[1])
	print(encPrint(strPrint))
# comments
#cur.execute("SELECT * FROM tblProjects ORDER BY comment DESC LIMIT 1")
#rows = cur.fetchall()
#for row in rows:
#	strPrint = str(row[1])
#	print(encPrint(strPrint))

# views
print("Projects with most views")
cur.execute("SELECT id, name, views FROM tblProjects ORDER BY views DESC LIMIT 10")
rows = cur.fetchall()
for row in rows:
	strPrint = str(row[1])
	print(encPrint(strPrint))

print("Most recently created")
# most recently created
cur.execute("SELECT id, name, created FROM tblProjects ORDER BY created DESC LIMIT 10")
rows = cur.fetchall()
for row in rows:
	strPrint = str(row[1])
	print(encPrint(strPrint))
	
# close connection
conn.close()
