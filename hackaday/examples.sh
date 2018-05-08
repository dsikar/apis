# As per https://dev.hackaday.io/doc/api/get-projects

# Retrieve key from /api-key - supplied by hackaday.io
APIKEY="$(cat api-key/plain-text-key)"

# Retrieve one project
# curl -G https://api.hackaday.io/v1/projects/1340?api_key=$APIKEY 
# Projects pagination
curl -G https://api.hackaday.io/v1/projects?api_key=$APIKEY&page=1&per_page=2
