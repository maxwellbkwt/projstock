import requests
import BeautifulSoup4 as bs
import json

def get_webmsg (year, month, stock_id):
    url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=' + date + '&stockNo=' + sid
    date = str (year) + "{0:0=2d}".format(month) +'01' ## format is yyyymmdd
    sid = str(stock_id)

    res =requests.post(url_twse,)
    soup = bs(res.text , 'html.parser')
    smt = json.loads(soup.text)     #convert data into json
    return smt