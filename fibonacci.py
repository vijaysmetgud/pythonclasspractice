def get_fibonacci(num):
    if num <= 2:
        return None
    first = 1
    second = 2
    fib_seq = []
    fib_seq.append(first)
    fib_seq.append(second)
    while True:
        third = first + second
        if third > num:
            return fib_seq
        fib_seq.append(third)
        first = second
        second = third
              
       
       
print(get_fibonacci(100))