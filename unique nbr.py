def list(a):
    i=0
    b=[]
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        i=i+1
    return b
a=[1,2,3,4,4,5,6,5,2]
print(list(a))