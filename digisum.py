number = 9655
q = 0
sum = 0
remainder = 0
while number >= 10: 
   remainder = number % 10
   sum = remainder + sum
   q = number // 10
   if q < 10:    
      sum = sum + q 
      break
   else:
      number = q   
if sum >= 10:
   z = 0
   y = 0
   y = sum % 10
   z = sum // 10
   sum = y + z   
print(sum) 
    