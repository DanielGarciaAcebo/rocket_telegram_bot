from datetime import datetime
import os

def translate_txt(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()





def get_current_datetime():
    """
    Returns the current date and time as a string.

    Format: 'YYYY-MM-DD HH:MM:SS'
    """
    current_datetime = datetime.now()
    return current_datetime.strftime('%Y-%m-%d %H:%M:%S')
