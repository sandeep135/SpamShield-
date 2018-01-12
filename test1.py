import requests
BASE_URL = "http://127.0.0.1:5000" 

years_exp = {"yearsOfExperience": 'RC 344 : Idea ka Best offer Kewal Aapke liye Payein Free Local STD calls aur 1GB data 4G handset par. Recharge today.'}

response = requests.post("{}/predict".format(BASE_URL), json = years_exp)

print(response.json())