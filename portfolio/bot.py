import requests

def send_message(text):
    url = f"https://api.telegram.org/bot6911927885:AAGiUz3gLQzehcawrjRWLkFSEPEaLhsrSlU/sendMessage"
    params = {"chat_id": '1776373061', "text": text}
    response = requests.post(url, data=params)
    return response.json()