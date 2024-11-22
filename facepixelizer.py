import requests
inp=input("enter the url:")
url = f"https://api.apilayer.com/face_pixelizer/url?url={inp}"

payload = {}
headers= {
  "apikey": "4A4ABHgeVE9KMB05A7k1cKFISOpRZ1HV"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)