
def Comphrehension ():
    list=[]
    for x in range(11):
        if(x==0):
            continue
        list.append(x**2) 
    return list

result=Comphrehension()
print(result)