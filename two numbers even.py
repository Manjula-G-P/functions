def even(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("both numbers are even")
        else:
            print("both numbers are not even")
        i=i+1
even(([2, 6, 18, 10, 3, 75]),([6, 19, 24, 12, 3, 87]))
