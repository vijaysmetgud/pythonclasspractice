if __name__ == '__main__':
    n = int(input("enter the value of n: "))
    if n % 2 != 0:
        print("odd")
    else:
          
        if n in range(2,5):
            print("in five") 
            
        elif n in range(6,20):  
            print("in twenty") 
            
        elif n > 20:
            print("over twenty")    

    