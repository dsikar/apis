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
        #print('key = ' + str(key))
        if str(key) == 'total':
            retval = value
    pass
    return retval

APIKEY=getApiKey()
#url = "https://api.hackaday.io/v1/search?api_key=%s&search_term=esp8266&page=PAGENUMBER&per_page=1" % (APIKEY)
url = "https://api.hackaday.io/v1/search?api_key=APIKEY&search_term=esp8266&page=PAGENUMBER&per_page=1";
urlcnt = url.replace("APIKEY", APIKEY);
urlcnt = urlcnt.replace("PAGENUMBER", "1");

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
urlcnt = urlWithAPI.replace("PAGENUMBER", "1");
iPgCnt = getPageCount(urlcnt)
#print(iPgCnt);

for x in range(1, 2): # (iPgCnt+1):
    url = getURLWithAPI();
    url = url.replace("PAGENUMBER", str(x));
    print(url)
    # get url

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

