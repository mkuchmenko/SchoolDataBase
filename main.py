import csv
from csv import DictWriter

with open("config.txt", "r") as file:
    min_score = int(file.read())
print(min_score)

with open('students.csv', "r", encoding='utf-8') as file:
    data=list(csv.DictReader(file, delimiter=","))
    for i in data:
        i['score']=int(i['score'])

retest_list=[]
for st in data:
    if st['score']<85:
        retest_list.append(st)

readnames=['id','name','surname','score']

with open("retest.csv", "w", newline="", encoding="utf-8") as csvfile:
    write=DictWriter(csvfile, fieldnames=readnames, delimiter=',')
    write.writeheader()
    write.writerows(retest_list)



