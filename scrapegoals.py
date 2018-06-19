from requests_html import HTMLSession
import config

session = HTMLSession()

url = 'https://www.sportinglife.com/football/live/vidiprinter'
r = session.get(url)

def ScrapeGoals():

    while True:
        vidiline = r.html.find('.vidiline', first=True)
        highlight = vidiline.find('.vidiline-highlight-score', first=True)

        if highlight:
            if highlight.text.lower()[:-2] == str(config.TEAM).lower():
                vidiline_message = vidiline.find('.vidiline-message', first=True)
                vidiline_time = vidiline.find('.vidiline-time', first=True)
                vidiline_player = vidiline_message.find('.vidiline-player', first=True)
                vidiline_otherteam = vidiline_message.find('span:not(.vidiline-time):not(.vidiline-highlight-event):not(.vidiline-highlight-score):not(.vidiline-player)', first=True)

                return f"[{vidiline_time.text}] | GOAL! {vidiline_player.text} | {highlight.text} vs {vidiline_otherteam.text}"

