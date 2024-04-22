import snoop
@ snoop


def is_even(number: int):
   if number <= 0:
      return False
   
   if number % 2 == 0: 
      print(number, end="-")
      print("is EVEN", end=", ") 
   else:
      print(number, end="-")
      print("is ODD", end=", ")   



for value in range(1, 10):
    is_even(value)
       

    