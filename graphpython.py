from pandas import read_csv
from matplotlib import pyplot
import datetime as datetime
import csv
import os
import os.path
from os import path

os.remove("infoformat.csv")
a = open("infoformat.csv", "w+")

intos = open("info.txt", "r")
values  =[]
dates = []
for x in intos.readlines():
    splits = x.split()
    if len(splits) == 3:
        values.append(splits[0])
        joint = splits[1]+" " + splits[2]
        dates.append(joint)
intos.close()

with open('infoformat.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    counter = 0
    for lcv in values:
        old = dates[counter]
        new = ""
        new = new + old[6:10] + "/"
        new = new + old[3:5] + "/"
        new = new + old[0:2] + " "
        new = new + old[11:]
        print(new)
        
        writer.writerow([new,lcv ])
        counter += 1

f.close()



series = read_csv('infoformat.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
series.plot()
pyplot.show()
