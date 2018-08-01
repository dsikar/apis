import sqlite3
# create database and tables for Fireclass app
# connect
conn=sqlite3.connect('hackaday.db')
strSQL = 'CREATE TABLE \'tblProjects\' (\'Title\' TEXT, \'Title2\' TEXT, \'stockcode\' TEXT, \'InMenu\' INTEGER, \'ImageMini\' TEXT, \'Image1\' TEXT, \'Image2\' TEXT, \'Image3\' TEXT, \'Image4\' TEXT, \'Image5\' TEXT, \'long\' TEXT, \'hasPDF\' TEXT, \'pageID\' INTEGER);' # PRIMARY KEY NOT NULL);'
#TODO finish building table create script
strSQL = 'Insert into tblProjects(id, owner_id, name, summary, views, '
    strSQL += 'skulls, followers, logs, details, instruction, created, updated)'
    strSQL += 'VALUES (' + str(myid) + ',' + str(owner_id) + ', "' + name + '", "'
 
# create pages table
conn.execute(strSQL)
# close connection
conn.close()
