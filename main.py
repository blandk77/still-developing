from pyrogram import Client, filters
from commands import zip_files, unzip_files
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Client("my_bot")

@app.on_message(filters.command("zip"))
def start_zip(client, message):
    try:
        message.reply("Please send the files you want to zip.")
    except Exception as e:
        logging.error(f"Error in start_zip: {e}")

@app.on_message(filters.command("unzip"))
def start_unzip(client, message):
    try:
        message.reply("Please reply to the zip file you want to unzip.")
    except Exception as e:
        logging.error(f"Error in start_unzip: {e}")

app.run()
