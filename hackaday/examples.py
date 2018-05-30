import pycurl
from io import BytesIO

# http://pycurl.io/docs/latest/quickstart.html
f=open("api-key/plain-text-key", "r")
APIKEY=f.read()
APIKEY=APIKEY.strip()
print(APIKEY)
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
print(body.decode('iso-8859-1'))

