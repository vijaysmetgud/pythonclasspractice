number = int(input("enter any value: "))
i = 2
while i < number:
   if number % i == 0:   
     
      print("not prime")
      break
   i += 1  
else:
   print("prime")  
  