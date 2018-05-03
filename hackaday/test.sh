# 1. Retrieve key from /api-key
APIKEY="$(cat api-key/plain-text-key)"
curl -G https://api.hackaday.io/v1/projects/1340?api_key=$APIKEY 
