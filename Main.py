import telebot
import requests

# بياناتك الخاصة التي لا تتغير
TOKEN = '5904781551:AAG7Cpue6H6qKrEiRw950UtdWqaWz7ouRbo'
MY_ID = 5904781551
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/3ewfduqh0ujc9oeol3vqslk8oqn4p53e"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 أهلاً بك يا مبرمج رامي. وكيل النشر الشامل جاهز الآن!\n\nأي شيء ترسله لي هنا، سأقوم بنشره تلقائياً في قنواتك، مدونتك، وحساباتك.")

@bot.message_handler(func=lambda message: True)
def handle_publish(message):
    # إشعار البدء لرامي فقط
    if message.chat.id == MY_ID:
        bot.reply_to(message, "⏳ جاري إرسال المحتوى للوكيل المركزي للنشر في كل المنصات...")
        
        # إرسال البيانات إلى Make.com
        payload = {
            "content": message.text,
            "platform": "all_social_media",
            "author": "Ramy DZ"
        }
        
        try:
            res = requests.post(MAKE_WEBHOOK_URL, json=payload)
            if res.status_code == 200:
                bot.send_message(MY_ID, "✅ تم النشر بنجاح في يوتيوب، تلغرام، والمدونة!")
            else:
                bot.send_message(MY_ID, f"⚠️ الوكيل استلم الرسالة لكن الرد كان: {res.status_code}")
        except Exception as e:
            bot.send_message(MY_ID, f"❌ فشل الاتصال بالوكيل: {e}")
    else:
        bot.reply_to(message, "عذراً، هذا البوت خاص بالمطور رامي فقط.")

bot.infinity_polling()
