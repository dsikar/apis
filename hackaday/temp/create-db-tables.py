import sqlite3
# create database and tables for Fireclass app
# connect
conn=sqlite3.connect('fireclass.db')
strSQL = 'CREATE TABLE \'tblPages\' (\'Title\' TEXT, \'Title2\' TEXT, \'stockcode\' TEXT, \'InMenu\' INTEGER, \'ImageMini\' TEXT, \'Image1\' TEXT, \'Image2\' TEXT, \'Image3\' TEXT, \'Image4\' TEXT, \'Image5\' TEXT, \'long\' TEXT, \'hasPDF\' TEXT, \'pageID\' INTEGER);' # PRIMARY KEY NOT NULL);'
# create pages table
conn.execute(strSQL)
strSQL = 'CREATE TABLE \'tblMenus\' (\'MenuMain\' TEXT NOT NULL, \'MenuSub\' TEXT, \'MenuID\' INTEGER);' # PRIMARY KEY NOT NULL);'
# create menus table
conn.execute(strSQL)
# close connection
conn.close()
