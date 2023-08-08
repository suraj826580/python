def Fibonacci (input):
    list=[0,1]
    while(len(list)<input):
        list.append(list[-1]+list[-2])
    return list

result=Fibonacci(5)    
print(result)