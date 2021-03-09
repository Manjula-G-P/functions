def speed(n):
    if n<=70:
        print("Ok")
    elif n>70:
        i=70
        c=0
        while i<n:
        
            c=c+1
            i=i+5
        print(c,"points")
        if c>12:
            print("licensed suspended")
n=int(input("enter a num:"))
speed(n)