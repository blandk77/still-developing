import os
import zipfile
from pyrogram import Client, filters
import logging

def zip_files(client, message):
    try:
        # Logic to zip files
        files = []  # Collect files from user
        zip_filename = message.text.split()[1] + ".zip"
        
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files:
                zipf.write(file)
        
        message.reply_document(zip_filename)
    except Exception as e:
        logging.error(f"Error in zip_files: {e}")
        message.reply("An error occurred while zipping the files.")

def unzip_files(client, message):
    try:
        # Logic to unzip files
        zip_file = message.reply_to_message.document.file_name
        
        if os.path.getsize(zip_file) < 4 * 1024 * 1024 * 1024:  # Less than 4GB
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall("unzipped_files")
            # Send unzipped files back to user
            message.reply("Files unzipped successfully.")
        else:
            message.reply("The zip file exceeds the size limit for unzipping.")
    except Exception as e:
        logging.error(f"Error in unzip_files: {e}")
        message.reply("An error occurred while unzipping the files.")
                      
