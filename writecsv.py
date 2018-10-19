# write data to csv
import csv
import os

path = "\path\filename.csv"

def push_data(datas):
  #check file is exist
  if ( os.path.isfile(path)):
    #write stock data
    for data in (datas['data']):
      with open(path, "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
        
  #not found file      
  else:
    #write fileds & data
    with open(path, "a") as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(datas['fields'])
      
    for data in (datas['data']):
      with open("stock.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
