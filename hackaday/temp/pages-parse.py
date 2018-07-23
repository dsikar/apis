import json
from pprint import pprint

with open('json_pages.php', 'r', encoding='utf-8') as f:
    data = json.load(f)

# get size of array
iSizeArray=len(data['pages'])

def InsertRow(Title, Title2, stockcode, InMenu, ImageMini, Image1,
        Image2, Image3, Image4, Image5, long, hasPDF, pageID):
    strSQL = 'Insert into tblPages(Title, Title2, stockcode, InMenu, ImageMini, '
    strSQL += 'Image1, Image2, Image3, Image4, Image5, long, hasPDF, pageID)'
    strSQL += 'VALUES ("' + Title + '","' + Title2 + '", "' + stockcode + '", '
    strSQL += str(InMenu) + ', "' + ImageMini + '", "' + Image1 + '", "'
    strSQL += Image2 + '", "' + Image3 + '", "' + Image4 + '", "' + Image5 + '", "'
    strSQL += long + '", "' + hasPDF + '", ' + str(pageID) + ');'
    print(strSQL.encode("utf-8"))


for x in range(0, iSizeArray):

 
    Title=data['pages'][x]['Title']
    Title2=data['pages'][x]['Title2']
    stockcode=data['pages'][x]['stockcode']
    InMenu=data['pages'][x]['InMenu']
    ImageMini=data['pages'][x]['ImageMini']
    Image1=data['pages'][x]['Image1']
    Image2=data['pages'][x]['Image2']
    Image3=data['pages'][x]['Image3']
    Image4=data['pages'][x]['Image4']
    Image5=data['pages'][x]['Image5']
    long=data['pages'][x]['long']
    hasPDF=data['pages'][x]['hasPDF']
    pageID=data['pages'][x]['pageID']
    InsertRow(Title, Title2, stockcode, InMenu, ImageMini, Image1,
            Image2, Image3, Image4, Image5, long, hasPDF, pageID)






