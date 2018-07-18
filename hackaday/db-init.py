import sys
import sqlite3
from pathlib import Path
mypath = 'db-store/hackaday.db'
myfile = Path(mypath)
if myfile.is_file():
    sys.exit()
conn = sqlite3.connect(mypath)
conn.close()
