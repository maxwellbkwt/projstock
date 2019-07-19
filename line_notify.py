#!venv/bin/python3

import requests
import twder

token = 'qq0EAfbf6KQArNZLR0SDGXLAbEqLV2uCNr3UM2hN599'

def lineNotifyMessage(token, msg):
    headers = {
            "Authorization": "Bearer " + token,
            "Content-Type" : "application/x-www-form-urlencoded"
            }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code


#message = "notify from my mac"
#token = 'rBYv97li5o19iz5Xx7kfQVwbH7W4vDtRV9xKAF1iGRd'
#token = 'qq0EAfbf6KQArNZLR0SDGXLAbEqLV2uCNr3UM2hN599'
#lineNotifyMessage(token,message)


def getUSDBuy():
    usd_price = twder.now('USD')
    cap_time = usd_price[0]
    usd_buy = usd_price[3]
    usd_sell = usd_price[4]
    print(usd_sell)
    if float(usd_sell) > 30:
        message = 'sell price ok, buy usd'
        lineNotifyMessage(token,message)


def main():
    getUSDBuy()

if __name__ == '__main__':
    main()
