#popular module use for api fetching data

import requests

response=requests.get(url=" https://api.covidtracking.com/v1/status.json")

print(response)

#it will chnage format to json
data=response.json()
print(data)

#it will show item of key in dictionary
runnumber=data["runNumber"]
print(runnumber)

response1=requests.get(url="https://api.covidtracking.com/v1/states/info.json")
print(response1.json())