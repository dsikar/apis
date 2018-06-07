import pycurl
from io import BytesIO
import json
from time import sleep

def pagenumber(a):
  print('last page = ' + str(a))

def getApiKey():
    f=open("api-key/plain-text-key", "r")
    APIKEY=f.read()
    APIKEY=APIKEY.strip()
    return APIKEY

def getPageCount():
    APIKEY=getApiKey()
    url = "https://api.hackaday.io/v1/search?api_key=%s&search_term=esp8266&page=1&per_page=1" % (APIKEY)
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
    jsonObject = json.loads(body.decode('iso-8859-1'))
    retval = 0
    for key in jsonObject:
        value = jsonObject[key]
        #print('key = ' + str(key))
        if str(key) == 'total':
            retval = value
    pass
    return retval

iPgCnt = getPageCount()

for x in range(iPgCnt+1):
    print(x) # iterate through all found pages, extracting as required
    sleep(0.2) # hackaday api allows 10 reads per sec, working with 5 to be on safe side
    # 1. todo parse string
    # 2. store - flat file or database
print(iPgCnt)
