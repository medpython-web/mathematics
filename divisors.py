def divisors(n):
    factors=[]
    for i in range(1,n):
         if n%i==0:
            factors.append(n//i)
    print(sorted(factors))


     


      

        

