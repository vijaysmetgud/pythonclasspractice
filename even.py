def is_even(number: int):
   if number <= 0:
      return False
   
   if number % 2 == 0: 
      print(number, end="-")
      print("EVEN", end=",") 
   else:
      print(number, end="-")
      print("ODD", end=" ")   



for value in range(1, 10):
    is_even(value)
       

    