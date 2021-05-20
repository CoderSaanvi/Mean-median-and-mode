import csv 
with open('HeightWeight2.csv',newline='') as f: 
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    n=fileData[i][1]
    newData.append(float(n))
totalData=len(newData)
total=0
for x in newData:
    total+=x
mean=total/totalData
print("Mean: ", mean)