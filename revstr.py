def string(user):
    a=" "
    i=-1
    while i>=-len(user):
        a=a+user[i]
        i=i-1
    return a
user=input("enter a str:")
print(string(user))