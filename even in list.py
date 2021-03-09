def even(n):
    i=0
    b=[]
    while i<len(n):
        if n[i]%2==0:
            b.append(n[i])
        i=i+1
    return b
        
        

print(even(([1,2,3,4,5,6,7,8])))