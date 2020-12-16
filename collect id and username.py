import requests


def collect(token=str()):
    user = dict()
    url_base = f'https://api.telegram.org/bot{token}/'
    historic = requests.post(url_base + "getUpdates")
    historic = historic.json()
    historic_chat = historic['result']
    for item in historic_chat:
        username = item['message']['from']['username']
        userid = item['message']['from']['id']
        user[username] = int(userid)
    print(user)


collect(token='The Bot token here')
