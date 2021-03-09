def perfect(n):
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if n==sum:
        print(n,"is a perfect nbr ")
    else:
        print(n,"is not a perfect nbr")
n=int(input("enter a nbr:"))
perfect(n)