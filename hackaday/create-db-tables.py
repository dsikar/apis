import sqlite3
# create database and tables for Fireclass app
# connect
conn=sqlite3.connect('hackaday.db')
strSQL = 'CREATE TABLE \'tblProjects\' (\'id\' INTEGER, \'owner_id\' INTEGER, \'name\' TEXT, \'summary\' TEXT, \'views\' INTEGER, \'skulls\' INTEGER, \'followers\' INTEGER, \'logs\' INTEGER, \'details\' INTEGER, \'instruction\' INTEGER, \'created\' INTEGER, \'updated\' INTEGER);' # PRIMARY KEY NOT NULL);'
# create pages table
conn.execute(strSQL)
# close connection
conn.close()


