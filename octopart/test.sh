# 1. Retrieve key from /api-key
EXAMPLE_KEY=(key key from filesystem)
curl -G http://octopart.com/api/v3/parts/match \
   -d queries="[{\"mpn\":\"SN74S74N\"}]" \
   -d apikey=$EXAMPLE_KEY \
   -d pretty_print=true
