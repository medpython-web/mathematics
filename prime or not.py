import math
def prime_number(n):
        for i in range(2,round(int(math.sqrt(n)))+1):
            if n%i!=0:
                    continue
            print("it's not a prime")
            break
        else :
              print("it's a prime")
                      
        prime_number(n=int(input("Enter a natural number: ")))
prime_number(n=int(input("Enter a natural number: ")))
  
     


      

        

