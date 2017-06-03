#Find the cube root of perfect cube

def go():
    x = int(input('Enter an int: '))
    ans = 0
    while ans**3 < abs(x):
        ans = ans + 1
    if ans**3 != abs(x):
        print (x, 'is not a perfect cube')
    else:
        if x < 0:
            ans = -ans
        print ('Cube root of ' + str(x) + ' is ' + str(ans))

def addupto(arg):
    max = arg
    i = 0
    while i < max:
        i = i + 1
    print (i)
