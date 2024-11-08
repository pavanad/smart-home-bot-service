import requests
from settings import GRACE_SERVICE_URL


def grace_service_invoke(message: str, chat_id: int) -> str:
    url = f"{GRACE_SERVICE_URL}/query"
    result = requests.post(url, json={"message": message, "chat_id": chat_id})

    if result.status_code != 200:
        raise Exception(f"Error invoking grace service: {result.text}")

    return result.json().get("result")
