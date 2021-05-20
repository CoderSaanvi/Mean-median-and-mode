import csv
with open('HeightWeight2.csv',newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    height=fileData[i][1]
    newData.append(height)
totalData=len(newData)
newData.sort()
if(totalData%2==0):
    median1=float(newData[totalData//2])
    median2=float(newData[totalData//2-1])
    median=(median1+median2)/2
else: 
    median=newData[totalData//2]
print("Median: ",median)