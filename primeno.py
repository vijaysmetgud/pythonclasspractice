def primeno(number):
    start = 2
    while start <= number:
        if number%start == 0:
          return False
        start = start + 1   
    return True        
print(primeno (17))   

     
 
 
  
