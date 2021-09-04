import requests

API_PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}
TRIVIA_API = "https://opentdb.com/api.php"

trivia_response = requests.get(url=TRIVIA_API, params=API_PARAMETERS)
trivia_response.raise_for_status()
question_data = trivia_response.json()["results"]

