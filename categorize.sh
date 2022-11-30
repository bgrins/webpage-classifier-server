
# A script for testing the server to be called like
# ./categorize.sh https://example.com
# It will use curl to get the HTML, jq to construct JSON as { "html": "...", "url": "..." }
# and then post to webpage_classifier_server and output the classification

webpage_classifier_server="http://localhost:8000" 
url=$1

if [ -z "$url" ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

html=$(curl -s $url)
json=$(echo $html | jq -R -s '{html: ., url: "'$url'"}')
curl -X POST $webpage_classifier_server -H "Content-Type: application/json" -d "$json"
