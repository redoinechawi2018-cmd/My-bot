import telebot
import requests
from flask import Flask
from threading import Thread
import os

# --- 1. إنشاء سيرفر وهمي لإرضاء Render ---
app = Flask('')

@app.route('/')
def home():
    return "الوكيل رامي يعمل بنجاح!"

def run():
    # Render يطلب العمل على المنفذ 10000 أو المنفذ المتغير
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- 2. إعدادات البوت والوكيل المركزي ---
TOKEN = '5904781551:AAG7Cpue6H6qKrEiRw950UtdWqaWz7ouRbo'
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/xi6yrdqpcdpjty9dqvwrvh3ykwwavvl0
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 الوكيل المركزي لرامي متصل وسيعمل نيابة عنك الآن!")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    # إرسال المنشور إلى Make.com للنشر في يوتيوب وفيسبوك والمدونة
    payload = {"content": message.text, "user": "Ramy"}
    try:
        requests.post(MAKE_WEBHOOK_URL, json=payload)
        bot.reply_to(message, "✅ تم إرسال المنشور للوكيل! سيتم النشر في جميع حساباتك فوراً.")
    except:
        bot.reply_to(message, "❌ فشل الاتصال بالمنفذ المركزي.")

# --- 3. تشغيل كل شيء ---
if __name__ == "__main__":
    keep_alive() # تشغيل السيرفر لإبقاء Render سعيداً
    bot.infinity_polling()
