x = 3
y = float(3)


values = [1,2,23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[5])

x = "this is a thing"
y = x.split( )
z = y[0]
print(y)
print(z)


x = input("Enter a message: ")
y = x.split( )

print(y)
print(len(y))

def calc(x):
    if x % 2 == 1:
        print("odd")
    else:
        print("even")

def tip(x):
    service = input("how was the service?: ")
    if service == "bad":
        x = x * 0
        print(f'${x} is your tip.')
    elif service == "okay":
        x = x * .15
        print(f'${x} is your tip.')
    elif service == "good":
        x = x * .20
        print(f'${x} is your tip.')
    elif service == "great":
        x = x * .25
        print(f'${x} is your tip.')
    else:
        print("Error, please try again.")


def factors(z,x):
    if z > x:
        print("End")
    else:
        if x % z == 0:
            print(z)
            z += 1
            factors(z,x)
        else: 
            z += 1
            factors(z,x)


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

gcf(30,60)