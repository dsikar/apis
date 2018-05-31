import pycurl
from io import BytesIO
import json
# http://pycurl.io/docs/latest/quickstart.html
f=open("api-key/supplier-compare", "r")
APIKEY=f.read()
APIKEY=APIKEY.strip()
url = "http://octopart.com/api/v3/parts/match?apikey=%s&queries=[{\"mpn\":\"SN74S74N\"}]&pretty_print=true" % (APIKEY)
print(url)
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
parsed_json = json.loads(body.decode('iso-8859-1'))
print(parsed_json)
# print(body.decode('iso-8859-1'))

