def test_range(n):
    if n in range(1,10):
        print(n,"is in the range")
    else:
        print(n,"is out of the range")
n=int(input('enter a num:'))
test_range(n)