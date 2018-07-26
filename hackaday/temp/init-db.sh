# init db
echo "Deleting fireclass.db sqlite3 database..."
rm fireclass.db
sleep 0.5
# create database and tables
echo "Creating fireclass database, pages and menus tables..."
python3 create-db-tables.py
sleep 0.5
# insert data
echo "Inserting menu data..."
python3 menus-parse.py
sleep 0.5
echo "Inserting pages data..."
python3 pages-parse.py
# display data
sleep 0.5
echo "Selecting inserted menu data..."
python333 menus-show-data.py
sleep 0.5
echo "Selecting inserted pages data..."
python3 pages-show-data.py
