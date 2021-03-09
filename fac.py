def fun(n):
    u=0
    l=0
    i=0
    while i<len(n):
        if n[i]>="a" and n[i]<="z":
            l=l+1
        elif n[i]>="A" and n[i]<="Z":
            u=u+1
        i=i+1
    print("no. of lower:",l)
    print("no of uper:",u)
n="The quick Brow Fox"
fun(n)