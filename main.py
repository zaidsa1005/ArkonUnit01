import logging
import os
import requests
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = "https://api.ankonbrain.ai/reply"

@app.route("/", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        user_message = data["message"]["text"]

        try:
            bot_reply = requests.post(API_URL, json={"message": user_message}, headers={"Content-Type": "application/json"}).text
        except Exception as e:
            bot_reply = "⚠️ حدث خطأ أثناء الاتصال بالذكاء البديل."

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": bot_reply}
        )
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)