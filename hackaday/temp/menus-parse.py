import sqlite3
import json
from pprint import pprint

with open('json_menus.php', 'r', encoding='utf-8') as f:
    data = json.load(f)

# get size of array
iSizeArray=len(data['menus'])

def ExecSQL(strSQL):
    conn=sqlite3.connect('fireclass.db')
    c = conn.cursor()
    print(strSQL)
    c.execute(strSQL)
    conn.commit()
    conn.close()
    
def InsertRow(MenuMain, MenuSub, MenuID):
    strSQL = 'Insert into tblMenus(MenuMain, MenuSub, MenuID) '
    strSQL += 'VALUES ("' + MenuMain + '","' + MenuSub + '", ' + str(MenuID) + ')'
    ExecSQL(strSQL)


for x in range(0, iSizeArray):
    MenuMain=data['menus'][x]['MenuMain']
    MenuSub=data['menus'][x]['MenuSub']
    MenuID=data['menus'][x]['MenuID']
    InsertRow(MenuMain, MenuSub, MenuID)






