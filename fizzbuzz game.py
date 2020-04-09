#fizzbuzz with while loop

num = 1
while(num<=100):
    
    if (num %3 ==0) and (num % 5 ==0):
        print("%s fizzbuzz" %num)
    
    elif (num % 3==0):
        print("%s fizz" %num)
       
    elif (num % 5==0):
        print("%s buzz" %num)
            
    else:
        print(num)
    num+=1
    
print("The game has ended, thanks for playing")


#fizzbuzz with for loop

for num in range(1,101):
    if (num %3 ==0) and (num % 5 ==0):
        print("%s fizzbuzz" %num)
    
    elif (num % 3==0):
        print("%s fizz" %num)
       
    elif (num % 5==0):
        print("%s buzz" %num)
            
    else:
        print(num)
    num+=1
    
print("The game has ended, thanks for playing")