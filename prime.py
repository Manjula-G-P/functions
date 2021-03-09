def prime(n):
    i=2
    c=0
    while i<=n:
        if n%i==0:
            c=c+1
        i=i+1
    if c==1:
        print(n,"is a prime nbr")
    else:
        print(n,"is not a prime nbr")
n=int(input("enter a num:"))
prime(n)