def fact(n):
    i=1
    f=1
    while i<=n:
        f=f*i
        i=i+1
    return(f)
n=int(input("enter a num:"))
print(fact(n))