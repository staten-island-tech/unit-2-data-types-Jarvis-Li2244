x = 3
y = float(3)


values = [1,2,23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[5])

x = "this is a thing"
y = x.split()
z = y[0]
print(y)
print(z)


x = input("Enter a message: ")
y = x.split()

print(y)
print(len(y))

def calc(x):
    if x % 2 == 1:
        print("odd")
    else:
        print("even")


def bill(x):
    x = input("What was your bill?: $")
    service = input("How was the service?: ")
    x = float(x)
    if service.lower() == "bad":
        y = x * 0
    elif service.lower() == "okay":
        y = x * .15
    elif service.lower() == "good":
        y = x * .20
    elif service.lower() == "great":
        y = x * .25
    else:
        print("That's not how the service was.. Try again.")
        bill(x)
    print(f'${y} is your tip.')
    y = int(y)
    print(f'Here is your total: ${y + x}')
bill(x)

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

