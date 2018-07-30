import pycurl
from io import BytesIO
import json
from time import sleep
import sys
import sqlite3

####################
# Hackaday scraper #
####################

# +-------+           +--------+
# |SCRAPER|           |HACKADAY|
# |ENGINE | +-------> |PROJECTS|
# +-------+           +----+---+
#                         |
#                         |
#                         v
#            +------------+-------------+
#            | * ID (UNIQUE KEY)        |
#            | * FOLLOWERS              |
#            | * ENTRIES (DOCUMENTATION)|
#            | * COMMENTS               |
#            +--------------------------+
#                         |
#                         |
#                         v
#                     Database

#####################################
# Base URL                          #
# Where we go to start our scraping #
#####################################

strBaseURL = "https://api.hackaday.io/v1/search?api_key=APIKEY&search_term=esp8266&page=PGNUM&per_page=1"; 

def pagenumber(a):
  print('last page = ' + str(a))

################################
# Read API key from filesystem #
################################

def getApiKey():
    f=open("api-key/plain-text-key", "r")
    APIKEY=f.read()
    f.close()
    APIKEY=APIKEY.strip()
    return APIKEY

##############################
# Retrieve text from webpage #
##############################

def getURLbody(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    # dev env workaround - https://stackoverflow.com/questions/8332643/pycurl-and-ssl-cert
    c.setopt(pycurl.SSL_VERIFYPEER, 0)   
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    c.setopt(c.URL, url) 
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    return body 

########################################################
# Retrieve the number of pages we will iterate through #
########################################################

def getPageCount(url):
    body = getURLbody(url) 
    retval = getKey('total', body);
    # print(retval)
    return retval

#############################################
# Retrieve value from a json key value pair #
#############################################

def getKey(myKey, body):
    jsonObject = json.loads(body.decode('iso-8859-1'))
    retval = 0;
    for key in jsonObject:
        value = jsonObject[key]
        if str(key) == myKey:
            retval = value
            break
    pass
    return retval

######################################
# Return base URL from function call #
######################################

def getBaseURL():
    return strBaseURL; 

######################
# Add API key to URL #
######################

def getURLWithAPI():
    url = getBaseURL();
    APIKEY=getApiKey();
    return url.replace("APIKEY", APIKEY)

# execute sql statement
def ExecSQL(strSQL):
    conn=sqlite3.connect('hackaday.db')
    c = conn.cursor()
    c.execute(strSQL)
    conn.commit()
    conn.close()

# Build insert string
def InsertRow(idx, Title, Title2, stockcode, InMenu, ImageMini, Image1,
        Image2, Image3, Image4, Image5, long, hasPDF, pageID):
    strSQL = 'Insert into tblPages(Title, Title2, stockcode, InMenu, ImageMini, '
    strSQL += 'Image1, Image2, Image3, Image4, Image5, long, hasPDF, pageID)'
    strSQL += 'VALUES ("' + Title + '","' + Title2 + '", "' + stockcode + '", '
    strSQL += str(InMenu) + ', "' + ImageMini + '", "' + Image1 + '", "'
    strSQL += Image2 + '", "' + Image3 + '", "' + Image4 + '", "' + Image5 + '", "'
    strSQL += long + '", "' + hasPDF + '", ' + str(pageID) + ');'
    if idx == 181: # problem Ω ohm character - needs fixing 
        print(strSQL.encode('utf-8'))
    elif pageID == 156:
        print('pageID 156 needs \n fixing (breaking json at the moment)')
    else:
        ExecSQL(strSQL)


# Go through pages

urlWithAPI = getURLWithAPI();
urlcnt = urlWithAPI.replace("PGNUM", "1");
iPgCnt = getPageCount(urlcnt)
print(iPgCnt);

for x in range(1, iPgCnt+1):
    url = urlWithAPI.replace("PGNUM", str(x));
    mybody = getURLbody(url);
    # print(mybody);
    # myproj = getKey('results', mybody);
    jsonObject = json.loads(mybody.decode('iso-8859-1'))
    total = jsonObject["total"];
    myid = jsonObject["results"][0]["id"];
    owner_id = jsonObject["results"][0]["owner_id"];
    name = jsonObject["results"][0]["name"];
    summary = jsonObject["results"][0]["summary"];
    views = jsonObject["results"][0]["views"];
    skulls = jsonObject["results"][0]["skulls"];
    followers = jsonObject["results"][0]["followers"];
    logs = jsonObject["results"][0]["logs"];
    details = jsonObject["results"][0]["details"];
    instruction = jsonObject["results"][0]["instruction"];
    created = jsonObject["results"][0]["created"];
    updated = jsonObject["results"][0]["updated"];
    strResults = str(myid) + "|" + str(owner_id) + "|" + name + "|" + summary + "|" 
    strResults += str(views) + "|" + str(skulls) +  "|" + str(followers) + "|" + str(logs) 
    strResults += "|" + str(details) + "|" + str(instruction) + "|" + str(created)
    strResults += "|" + str(updated)
    print(strResults)
    # sleep for a few seconds
    sleep(5)

