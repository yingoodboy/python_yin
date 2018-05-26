# coding = utf-8
from datetime import datetime
import os
os.getcwd()
uriage = {}
sum = 0
sum6 = 0
sum7 = 0
with open("/home/centos/code/test003.txt") as cl:
    for line in cl:
        dateStr, item, valueStr = line.split(',') 
        date = datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S") 
       
        #dateA = datetime.strptime("20150601 00:00:00", "%Y%m%d %H:%M:%S")
        #dateB = datetime.strptime("20150701 00:00:00", "%Y%m%d %H:%M:%S") 
        #dateC = datetime.strptime("20150601 13:00:10", "%Y%m%d %H:%M:%S")

        if (datetime(2015, 6, 1) <= date < datetime(2015, 7, 1)):
            month = "6月"
            
        elif (datetime(2015, 7, 1) <= date < datetime(2015, 8, 1)):
            month = "7月"
        else:
            pass
        #print(time)
        #print(value)
        #sum += int(value)
        #print(sum)     
        if month in uriage:
             uriage[month] += int(valueStr)
        else:
             uriage[month] = int(valueStr)
    for key, val in uriage.items():
        print("{}: {}" .format(key,val))
    #print(sum6)         
    #print(sum7)

        #time, item, value = line.split(',')
        #sum += int(value)
        #print(sum)

        

