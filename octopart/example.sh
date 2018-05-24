# 1. Retrieve key from /api-key
APIKEY="$(cat api-key/supplier-compare)"
curl -G http://octopart.com/api/v3/parts/match \
   -d queries="[{\"mpn\":\"SN74S74N\"}]" \
   -d apikey=$APIKEY \
   -d pretty_print=true
# Another part
curl -G http://octopart.com/api/v3/parts/match \
   -d queries="[{\"mpn\":\"AT90USB1289\"}]" \
   -d apikey=$APIKEY \
   -d pretty_print=true
