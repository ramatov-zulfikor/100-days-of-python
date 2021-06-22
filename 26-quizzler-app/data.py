import requests

parameters = {
    "amount": 15,
    "category": 18,
    "difficulty": "easy",
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
