def fact(n):
    c=1
    for i in range(1,n+1):
        c=i*c

    print ("factorial of",n,"is :", c )

fact(10)