def ListCreator (initialValue=1):
    list=[]
    count=initialValue
    while(count<=initialValue+10):
        list.append(count)
        count+=1
    return list

result=ListCreator(10)

result.append(4)
print(result)

result.pop()
print(result)

result.sort(reverse=True)
print(result)