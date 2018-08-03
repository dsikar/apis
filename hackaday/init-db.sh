# init db
echo "Deleting fireclass.db sqlite3 database..."
rm hackaday.db
sleep 0.5
# create database and tables
echo "Creating fireclass database, pages and menus tables..."
python create-db-tables.py
sleep 0.5
# insert data
echo "Inserting hackaday data..."
python scan.py
sleep 0.5
# display data
echo "Displaying inserted hackaday data..."
python hackaday-show-data.py
