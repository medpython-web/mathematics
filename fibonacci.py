def fibonaacii(n):
    a=0
    b=1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    print()
fibonaacii(4)
