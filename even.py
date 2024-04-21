def is_even(number: int):
   if number <= 0:
      return False
   if number % 2 == 0: 
      return number



for index in range(10,25):
   if is_even(index):
       print(index,end="  ")

    