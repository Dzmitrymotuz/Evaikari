from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from ai import *


load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_ID = os.getenv("BOT_ID")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Да я тут просто Ева, обычная женщина, отвечаю на сообщения в чате. Не надо паранойи разводить, спрашивай, что хочешь.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Помогу чем угодно, я не против поболтать и поддержать разговор. Что тебя интересует? Надо совета, поддержки или просто поговорить обо всем на свете? Готова выслушать и поддержать, братишка!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is custom command')

# Responses 
def handle_response(text:str)->str:
    processed: str = text.lower()
    try:
        response = send_request(processed)
        print(response.content)
        return response.content
    except Exception as e:
        return f"Error occurred: {str(e)}"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # print('message ',message_type, 'TEXT: ', text)
    print(update.message.reply_to_message)

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}')
    if message_type == 'supergroup':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        elif "ева" in text.lower():
            response: str = handle_response(text)
        elif update.message.reply_to_message and update.message.reply_to_message.from_user.username == 'evaikari_bot':
            response: str = handle_response(text)
        else:
            return  
    if message_type == 'private': 
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        elif "ева" in text.lower():
            response: str = handle_response(text)
        elif update.message.reply_to_message and update.message.reply_to_message.from_user.username == 'evaikari_bot':
            response: str = handle_response(text)
        else:
            return  
            response: str = handle_response(text) 
    else:
        if BOT_USERNAME in text:
            response: str = handle_response(text)

    await update.message.reply_text(response)

async def error(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(API_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)