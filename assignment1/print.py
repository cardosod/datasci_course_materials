import urllib
import json

#response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
response = urllib.urlopen("https://api.twitter.com/1.1/search/tweets.json?q=microsoft")
pyresponse = json.load(response)
print pyresponse

#print pyresponse.keys()

#results = pyresponse["results"]
#print results
#print type(results)

#for i in range (0, len(results)):
#	print results[i]["text"]

