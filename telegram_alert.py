import os
import requests

API_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_message_to_telegram(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()

# bot = Bot(token=API_TOKEN)
# asyncio.run(bot.send_message(chat_id=CHAT_ID,text="This is a test msg for bot"))
def test_call():
    send_message_to_telegram("This is a test msg for bot")
    print("Done !")

