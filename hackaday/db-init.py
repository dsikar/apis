import sys
import sqlite3
from pathlib import Path
from io import BytesIO

mypath = 'db-store/hackaday.db'
myfile = Path(mypath)
if not myfile.is_file():
    print('did not find db file')
    sys.exit()
conn = sqlite3.connect(mypath)
# load file
f=open('db-store/projects-table.sql', 'r')
mysql=f.read()
f.close()
print(mysql)
# execute
# close
conn.close()
