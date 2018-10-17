#for test ,first time get stock history 
import requests
import json
import datetime
import csv

dt = datetime.datetime.now()
count = 1

id_list = ['2454']
year_list = range(2018, dt.year+1)
month_list = range(1, 13)

for stock in id_list:
    for year in year_list:
        for month in month_list:
            if ((year == dt.year) and (month > dt.month)):
                break

            date = str(year) + "{0:0=2d}".format(month) + '01'
            url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+date+'&stockNo='+stock
            res = requests.get(url_twse)
            s = json.loads(res.text)
            if count == 1:
                with open("/Users/nick/Desktop/"+stock+".csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(s['title'])
                    writer.writerow(s['fields'])

            for data in (s['data']):
                print(data)

                with open("/Users/nick/Desktop/"+stock+".csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(data)
            count +=1
