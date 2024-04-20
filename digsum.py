number = 9999995
q = 0
sum = 0
remainder = 0
while number >= 10: 
   remainder = number % 10
   sum = sum + remainder
   q = round(number / 10)
   if q < 10:    
      break
   else:
      number = q   
print(sum) 
    
 