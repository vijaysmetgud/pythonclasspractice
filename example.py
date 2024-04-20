def project1():
    start = 1
    sum = 0
    while start <= 1000:
        if start % 3 == 0 or start % 5 == 0:
            sum = sum + start
        start += 1
    print (sum)
project1()
        
        
    
    