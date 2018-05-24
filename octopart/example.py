import pycurl
from io import BytesIO
import subprocess

# http://pycurl.io/docs/latest/quickstart.html

proc = subprocess.check_output("cat api-key/supplier-compare", shell=True)
proc = proc[:-1]
# print(proc)
url = "http://octopart.com/api/v3/parts/match?apikey=%proc" % (proc)
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
# print(body.decode('iso-8859-1'))

# 1. Retrieve key from /api-key
#APIKEY="$(cat api-key/supplier-compare)"
#curl -G http://octopart.com/api/v3/parts/match \
#   -d queries="[{\"mpn\":\"SN74S74N\"}]" \
#   -d apikey=$APIKEY \
#   -d pretty_print=true
