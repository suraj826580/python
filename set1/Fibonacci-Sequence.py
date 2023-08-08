def fibonacci(input):
    list=[0,1]
    count=0
    while(count<=input):    
        sum=list[-1]+list[-1]
        list.append(sum)
        count+=1
    return list

result=fibonacci(5)
print(result)

