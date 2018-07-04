import pycurl
from io import BytesIO
import json
from time import sleep

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

# Go through pages

urlWithAPI = getURLWithAPI();
urlcnt = urlWithAPI.replace("PGNUM", "1");
iPgCnt = getPageCount(urlcnt)
#print(iPgCnt);

url = getURLWithAPI();
for x in range(1, 2): # (iPgCnt+1):
    url1 = url.replace("PGNUM", str(x));
    mybody = getURLbody(url1);
    # print(mybody);
    # myproj = getKey('results', mybody);
    jsonObject = json.loads(mybody.decode('iso-8859-1'))
    print(jsonObject["total"]);
    print(jsonObject["results"][0]["id"]);
    print(jsonObject["results"][0]["owner_id"]);
    print(jsonObject["results"][0]["name"]);
    print(jsonObject["results"][0]["summary"]);
    print(jsonObject["results"][0]["views"]);
    print(jsonObject["results"][0]["skulls"]);
    print(jsonObject["results"][0]["followers"]);
    print(jsonObject["results"][0]["logs"]);
    print(jsonObject["results"][0]["logs"]);
    print(jsonObject["results"][0]["details"]);
    print(jsonObject["results"][0]["instruction"]);
     





    
    #myresults = jsonObject
    # print(jsonObject["results"][0]["id"]);
    #myId = getKey('id', myproj);
    #myFollowers = getKey('followers', myproj);

    # sleep for a few seconds
    sleep(5)


# TODO 1. Split functions:
#       1.1 Generate pycurl request string
#       1.2 Stringbuilder
#       1.3 Json Parser

#for x in range(iPgCnt+1):
#    print(x) # iterate through all found pages, extracting as required
#    sleep(0.2) # hackaday api allows 10 reads per sec, working with 5 to be on safe side
    # Lower priority (equally important) TODO 2. store - flat file or database

