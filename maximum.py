def fun(a,b,c):
    if a>=b and a>=c:
        largest=a
    elif b>=a and b>=c:
        largest=b
    else:
        largest=c
    return largest
largest=fun(10,14,20)
print("the max is:",largest)