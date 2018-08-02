import sqlite3
import json
import codecs
from pprint import pprint

#with open('json_text.php', 'r', encoding='utf-8') as f:
#    data = json.load(f)

data = json.load(codecs.open('json_text.php', 'r', 'utf-8-sig'))    

# get size of array
iSizeArray=len(data['Text'])

def ExecSQL(strSQL):
    conn=sqlite3.connect('fireclass.db')
    c = conn.cursor()
    # print(strSQL)
    c.execute(strSQL)
    conn.commit()
    conn.close()
    
def InsertRow(Label, Text):
    strSQL = 'Insert into tblText(Label, Text) '
    strSQL += 'VALUES ("' + Label + '","' + Text + '")'
    ExecSQL(strSQL)


for x in range(0, iSizeArray):
    Label=data['Text'][x]['Label']
    Text=data['Text'][x]['Text']
    InsertRow(Label, Text) 		






