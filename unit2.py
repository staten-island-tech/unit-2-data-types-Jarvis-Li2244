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


x = "placeholder message"
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
        x = x * 0.00
        print(f'${x} is your tip.')
    elif service == "okay":
        x = x * .15
        print(f'${x} is your tip.')
    elif service == "good":
        x = x * .20
        print(f'${x} is your tip.')
    else:
        x = x * .25
        print(f'${x} is your tip.')

tip(32638)
