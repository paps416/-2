import ollama
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

# token import
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

if not TELEGRAM_TOKEN:
    raise ValueError("token is missing")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def chat(message):
    chat_id = message.chat.id
    user_input = message.text

    # typing inc
    bot.send_chat_action(chat_id, 'typing')
    
    response = ollama.chat(
        model="dolphin-llama3",
        messages=[{"role": "user", "content": user_input}]
    )
    
    assistant_reply = response["message"]["content"]
    
    # response
    bot.send_message(chat_id, assistant_reply)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat(message)

if __name__ == "__main__":
    print("Bot is ready")
    bot.infinity_polling()