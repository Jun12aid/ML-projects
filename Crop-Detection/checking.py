import json
import requests

input_data = {
    "Soil_color": 0,
    "Nitrogen": 40,
    "Phosphorus": 20,
    "Potassium": 25,
    "pH": 7,
    "Temperature": 25,
    "Crop": 5,
}
url = "https://finalapi-y8ln.onrender.com/predict"

json_object = json.dumps(input_data)
response = requests.post(url,data=json_object)

print(response.text)