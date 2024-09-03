import json
import os
import random
import sqlite3
from datetime import datetime

import requests

from .. import settings


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


def send_photo(photoUrl, conversation_id):
    url = str(settings.URL + "sendPhoto")

    number = conversation_id.split(":")[-1]

    data = {
        "chat_id": number,
        "photo": photoUrl
    }

    response = requests.post(url, data=data)

    if response.status_code != 200:
        rpn = json.loads(response.text)
        return rpn
    else:
        return True


def get_random_id(used_ids):
    while True:
        random_id = random.randint(1, 123)
        if random_id not in used_ids:
            return random_id

def get_photo_by_id(photo_id):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "../bd/data_base.db")

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute('''
            SELECT url, rocket_lunch FROM photos WHERE id = ?
        ''', (photo_id,))


    result = cursor.fetchone()

    conn.close()

    if result:
        url, rocket_lunch = result
        return url, rocket_lunch
    else:
        return None, None
