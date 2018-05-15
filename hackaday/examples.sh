# As per https://dev.hackaday.io/doc/api

# Retrieve key from /api-key - supplied by hackaday.io
APIKEY="$(cat api-key/plain-text-key)"

# search
#curl -G https://api.hackaday.io/v1/search?api_key=$APIKEY&search_term=esp8266&page=1&per_page=1
# Retrieve one project
# curl -G https://api.hackaday.io/v1/projects/1340?api_key=$APIKEY 
# Projects pagination
# curl -G https://api.hackaday.io/v1/projects?api_key=$APIKEY&page=1&per_page=2
# Users
curl -G http://api.hackaday.io/v1/users?api_key=$APIKEY
