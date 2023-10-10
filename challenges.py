def tip(x):
    service = input("How was the service? : ")
    if service == "bad":
        y = x * 0
        print(f'${y} is your tip.')
    elif service == "okay":
        y = x * .15
        print(f'${y} is your tip.')
    elif service == "good":
        y = x * .20
        print(f'${y} is your tip.')
    elif service == "great":
        y = x * .25
        print(f'${y} is your tip.')
    else:
        print("Error, please try again.")


def factors(a,x):
    if a > x:
        print("No More Factors")
    else:
        if x % a == 0:
            print(a)
            a += 1
            factors(a,x)
        else: 
            a += 1
            factors(a,x)


def test(x):
    for z in range(1, x):
        if x % z == 0:
                print(z)
                z += 1
        else: 
                z += 1

def gcf(x,y):
    for z in range(x,0):
        if x % z == 0:
                if y % z == 0:
                     print(z)
                else:
                    z -= 1
        else: 
            z -= 1

def gcd(x, y):
    while(y):
        x, y = y, x % y
    print(x)
    return abs(x)

