import requests
#from bs4 import BeautifulSoup as bs
import json
#http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=201801&stockNo=2454
def get_webmsg (year, month, stock_id):
    date = str (year) + "{0:0=2d}".format(month) +'01' ## format is yyyymmdd
    print(date)
    sid = str(stock_id)
    url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=' + date + '&stockNo=' + sid

    res =requests.post(url_twse,)
#    soup = bs(res.text , 'html.parser') #covert to json
    smt = json.loads(res.text)     #convert data into json
    fileds = smt['fields']
    data=smt['data']
    print(data)
    return smt