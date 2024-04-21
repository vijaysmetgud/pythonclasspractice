def is_prime(number):
  i = 2
  while i < number:
    if number % 2 == 0 or number % i == 0:
      print("Notprime")    
      break
    i += 1 
    
  else:
    print("prime") 
    
  print(number)    
  
    
        
        
        
        
        
is_prime(12)
      
        