def countVowel(input):
    vowels = 0
    for char in input:
        if(char=="a" or char=="e" or char=="i" or char =="o" or char=="u"):
            vowels+=1
    print("Number of Vowels:",vowels) 
countVowel("Hello")    