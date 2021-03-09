def pan(n):
    a=""
    i=-1
    while i>=-len(n):
        a=a+n[i]
        i=i-1
    print(a)
    if n==a:
        print("the string is a palindrome")
    else:
        print("not a palindrome")
n=input("enter a string:")
pan(n)