#!/bin/bash

# init db

# delete if exists
echo "Deleting fireclass.db sqlite3 database..."
rm fireclass.db
sleep 0.5
# create database and tables
echo "Creating fireclass database, pages and menus tables..."
python create-tables.py
sleep 0.5
echo "Inserting menu data..."
python menus-parse.py
sleep 0.5
echo "Inserting pages data..."
python pages-parse.py
sleep 0.5
echo "Selecting inserted data..."
# todo

