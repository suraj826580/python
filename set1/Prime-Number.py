
def checkPrime(number):
     if(number==1):
        return "Not Prime"
     count=0
     for num in range(number):
          if number % (num+1)==0:
               count+=1
     if(count==2):
      return f"{number} is a Prime Number"
     else :
      return f"{number} is not a Prime Number"

result=checkPrime(13)
print(result)