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

def GcF(x,y):
    if x > y :
        z = y
    else: 
        z = x
    while z >= 1:
        if x % z == 0:
            if y % z == 0:
                return print(z)
            else:
                z -= 1
        else: 
            z -= 1
#GcF(48,672)

def gcd(x, y):
    while(y):
        x, y = y, x % y
    print(x)
    return abs(x)

#gcd(48, 372)
