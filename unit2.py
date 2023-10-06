'''
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
'''

def calc(x):
    if x % 2 == 1:
        print("odd")
    else:
        print("even")
#calc(263)

def bill():
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
    y = int(y)
    print(f'${y} is your tip.')
    print(f'Here is your total: ${y + x}')
#bill()

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
#factors(1,24)

def GcF(x,y):
    if x > y:
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
#GcF(720,3234)

