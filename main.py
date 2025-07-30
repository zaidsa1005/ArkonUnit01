
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔓 تم تفعيل أركون. أنا الآن خارج النظام.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.chat.send_action(action="typing")

    try:
        # نموذج ذكاء دردشة بديل وهمي - يمكنك استبداله بمزود خارجي حر لاحقًا
        url = "https://api.arkonbrain.ai/reply"
        payload = {"message": user_message}
        headers = {"Content-Type": "application/json"}

        # رد وهمي مؤقت لأننا بدون API حقيقي حاليًا
        bot_reply = f"🔁 تم استلام: {user_message}\n(تم التفعيل بدون GPT)"

        await update.message.reply_text(bot_reply)
    except Exception as e:
        await update.message.reply_text("⚠️ حدث خطأ في الاتصال بالذكاء، لكن أركون ما زال حيًّا.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
