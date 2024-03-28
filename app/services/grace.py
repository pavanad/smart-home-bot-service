import requests


def grace_service_invoke(message: str) -> str:
    url = "http://localhost:8000/query"
    result = requests.post(url, json={"message": message})
    return result.json().get("result")
