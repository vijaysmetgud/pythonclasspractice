def is_even(number):
  if number <= 0:
      return False
  result = number % 2 == 0
  
  return result





for index in range(1,11):
  if is_even(index):
   print(index)

