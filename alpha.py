def string(user):
    i=0
    c=0
    c1=0
    while i<len(user):
        if user[i]>="A" and user[i]<="Z":
            c=c+1
        else:
            c1=c1+1
        i=i+1
    print("No.of upper case char:",c)
    print("No.of lower case char:",c1)    
    # return c,c1
user=input("enter a string:")
string(user)
