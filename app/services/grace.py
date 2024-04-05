import requests
from settings import GRACE_SERVICE_URL


def grace_service_invoke(message: str) -> str:
    url = f"{GRACE_SERVICE_URL}/query"
    result = requests.post(url, json={"message": message})
    return result.json().get("result")
