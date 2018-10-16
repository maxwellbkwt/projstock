# write data to csv
import csv

with open("stock.csv", "a") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(smt['title'])
  writer.writerow(smt['fields'])
  
  for data in (s['data']):
    with open("stock.csv", "a") as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(data)
