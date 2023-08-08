def ListCreator (initialValue=1):
    list=[]
    count=initialValue
    while(count<=40):
        list.append(count)
        count+=10
    return list

result=ListCreator(10)

def Sum_Average(list):
    sum =0
    count=0
    for number in list:
        sum=sum+number
        count=count+1
    return {"Sum":sum,"average":sum/count}  
    
sumResult=Sum_Average(result)
for i in sumResult:
    print(i,sumResult[i])
    

