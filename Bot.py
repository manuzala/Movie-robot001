import telebot
import os

API_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot Render par live chhe! ✅")

@bot.message_handler(func=lambda message: True)
def forward_to_channel(message):
    try:
        bot.send_message(CHANNEL_ID, message.text)
        bot.reply_to(message, "Message channel ma mokli didho chhe!")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.polling()
