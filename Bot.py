import telebot
import os
import http.server
import socketserver
import threading

def listen_port():
    port = int(os.environ.get("PORT", 8080))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=listen_port, daemon=True).start()

API_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot Render par live chhe! ✅")

@bot.message_handler(func=lambda message: True)
def forward_to_channel(message):
    try:
        if CHANNEL_ID:
            bot.send_message(CHANNEL_ID, message.text)
            bot.reply_to(message, "Message channel ma share thai gayo!")
        else:
            bot.reply_to(message, "Error: CHANNEL_ID set nathi.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()
