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

