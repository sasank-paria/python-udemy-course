import json

import requests

url = "https://free-news.p.rapidapi.com/v1/search"

querystring = {"q":"covid 19","lang":"en"}

headers = {
	"X-RapidAPI-Host": "free-news.p.rapidapi.com",
	"X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response1=response.json()

# #it converts dictionary to
#
# jsonobj=json.dumps(response1)
# print(jsonobj)
#
# #method no 2 for dict to json
# with open("news.json", "w") as outfile:
#     json.dump(response1, outfile)


data=(response.json()['articles'][2]['summary'])
print(data)