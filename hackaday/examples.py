# TODO user python curl equivalent
# As per https://dev.hackaday.io/doc/api

# Retrieve key from /api-key - supplied by hackaday.io
# APIKEY="$(cat api-key/plain-text-key)"

# search
#curl -G https://api.hackaday.io/v1/search?api_key=$APIKEY&search_term=esp8266&page=1&per_page=1
# Retrieve one project
# curl -G https://api.hackaday.io/v1/projects/1340?api_key=$APIKEY 
# Projects pagination
# curl -G https://api.hackaday.io/v1/projects?api_key=$APIKEY&page=1&per_page=2
# Users
# curl -G http://api.hackaday.io/v1/users?api_key=$APIKEY
import pycurl
from io import BytesIO
import subprocess

# http://pycurl.io/docs/latest/quickstart.html

APIKEY = subprocess.check_output("cat api-key/plain-text-key", shell=True)
APIKEY = APIKEY[:-1]
# print(proc)
url = "https://api.hackaday.io/v1/search?api_key=%APIKEY&search_term=esp8266&page=1&per_page=1" % (APIKEY)
print(url)
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.io/')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))

