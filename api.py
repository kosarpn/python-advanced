import requests
phone=input("number:")
url = f"https://api.apilayer.com/number_verification/validate?number={phone}"

payload = {}
headers= {
  "apikey": "4A4ABHgeVE9KMB05A7k1cKFISOpRZ1HV"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
# result=response.text
print(result['valid'])
print(result['carrier'])
print(result['country_name'])