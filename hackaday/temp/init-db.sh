# init db
echo "Deleting fireclass.db sqlite3 database..."
rm fireclass.db
sleep 0.5
# create database and tables
echo "Creating fireclass database, pages and menus tables..."
python create-db-tables.py
sleep 0.5
# insert data
echo "Inserting menu data..."
python menus-parse.py
sleep 0.5
echo "Inserting pages data..."
python pages-parse.py
# display data
sleep 0.5
echo "Selecting inserted menu data..."
python menus-show-data.py
sleep 0.5
echo "Selecting inserted pages data..."
python pages-show-data.py
