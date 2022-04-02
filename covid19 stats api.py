import requests

url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country":"India"}

headers = {
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com",
	"X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.json())
print(response.json()['response'][0]['cases'])
print("active:",end="")
print(response.json()['response'][0]['cases']['active'])
print("critical:",end="")
critical_data=(response.json()['response'][0]['cases']['critical'])
print("recovered:",end="")
print(response.json()['response'][0]['cases']['recovered'])
print("total:",end="")
print(response.json()['response'][0]['cases']['total'])
