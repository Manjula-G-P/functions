print("welcome to state bank....!")
print("please insert ur card....")
atmpin=9999
def language():
    lang=input("plz select ur language:")
    if lang==1:
        print("english")
    elif lang==2:
        print("kannada")
def trans():
    p=int(input("enter ur pin nbr:"))
    print(type(trans),type(atmpin))
    if p==atmpin:
        print("1.withdraw")
        print("2.bal_eq")
        print("3.pin change")
        print("4.deposite")
        tran=int(input("choose a transaction:"))
        if tran==1:
            amt=int(input("enter ur amout:"))
            if amt>0:
                print("please collect ur cash")
        elif tran==2:
            slip=input("do u want a slip:")
            if slip=="y":
                print("take a slip")
            else:
                print("this ur balance")
        elif tran==3:
            op=int(input('enter ur old pin'))
            if op==atmpin:
                np=int(input('enter ur new pin:'))
                print("succesfully ur pin updated")
            else:
                print('invalid pin nbr')
    else:
        print('incorrect pin number')
language()
trans()


                