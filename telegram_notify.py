import requests
import sys
import os

def send_telegram_message(message):
    token = os.environ.get("7970951683:AAH8Uw_cCKNIngN-HEqhmnxgYrZrWS0vDqQ")
    chat_id = os.environ.get("729224032")
    if not token or not chat_id:
        print("Telegram token or chat ID not set")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload)

if __name__ == "__main__":
    message = sys.argv[1] if len(sys.argv) > 1 else "No message"
    send_telegram_message(message)
