
import math
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    Filedata = list(reader)


data = Filedata[0]

def mean(data):
    rag= len(data)
    total =0
    for hi in data:
        total += int(hi)

    mean = total / rag
    return mean


squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)



sum =0
for i in squared_list:
    sum =sum + i


result = sum/ (len(data)-1)



std = math.sqrt(result)
print(std)

