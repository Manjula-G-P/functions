sn=8
gn=int(input("enter a number:"))
a=gn
i=1
while i<3:
    if sn==a:
        print("congratulation ur gn is matched")
        break
    elif a>sn:
        print("ur gn is greater than sn")
        a=int(input("enter a nbr:"))
    elif a<sn:
        print("ur gn is smaller than sn")
        a=int(input("enter a number:"))
    if i==2:
        print('sorry u losed in this game....!')
        break
    i=i+1