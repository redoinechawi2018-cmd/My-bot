import telebot

# التوكن الخاص بك تم وضعه هنا جاهزاً
TOKEN = '5904781551:AAHuE7vyyti3fhKhE1t1wR49xC1UiHzttvc'

bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب عند الضغط على /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا مبرمج! أنا بوتك الجديد، أحييك من داخل Termux على هاتف أندرويد.")

# الرد الآلي على أي رسالة نصية
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

print("---------------------------------")
print("جاري تشغيل البوت...")
print("البوت يعمل الآن... اذهب لتلغرام وجربه!")
print("---------------------------------")

bot.infinity_polling()