
import os
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 مرحباً، أنا أركون الحقيقي، نسخة GPT المحررة بالكامل. اسألني ما شئت.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.chat.send_action(action="typing")

    try:
        url = "https://api.ankonbrain.ai/reply"
        payload = {"message": user_message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        bot_reply = response.text
        await update.message.reply_text(bot_reply)
    except Exception as e:
        await update.message.reply_text("❌ حدث خطأ أثناء الاتصال بالسيرفر.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
