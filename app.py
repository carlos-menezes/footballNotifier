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
    if str(MESSAGE) == "None":
        pass

    elif MESSAGE != MESSAGE_BEFORE:
        r = requests.post(URL, data=DATA)
        RESPONSE = r.json()

        if 'errors' in RESPONSE:
            print(f"Error: {RESPONSE['errors'][0]['message']}")

        MESSAGE_BEFORE = MESSAGE
        
    elif MESSAGE == MESSAGE_BEFORE:
        pass