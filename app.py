import requests
import config
import scrapegoals
import time

MESSAGE_BEFORE = ""
MESSAGE = scrapegoals.ScrapeGoals()

DATA = {
    "apikey": config.API_KEY,
    "numbers": config.NUMBER,
    "sender": config.SENDER,
    "message": MESSAGE 
}

URL = "https://api.txtlocal.com/send/"

while True:
    r = requests.post(URL, data=DATA)
    RESPONSE = r.json()

    if MESSAGE != MESSAGE_BEFORE:
        if 'errors' in RESPONSE:
            print(f"Error: {RESPONSE['errors'][0]['message']}")

        MESSAGE_BEFORE = MESSAGE
    

    time.sleep(60)
