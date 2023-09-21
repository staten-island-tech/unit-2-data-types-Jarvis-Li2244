def gcf(x,y):
    if x > y:
        b = x
    else:
        b = y
    for z in range(1, b):
        if x % z == 0:
            if y % z == 0:
                a = z
    return a
print(gcf(10,50))

def GcF(z,x,y):
    if z < 1:
        print("End")
    else:
        if x % z == 0:
            if y % z == 0:
                print(z)
            else:
                z -= 1
                GcF(z,x,y)
        else: 
            z -= 1
            GcF(z,x,y)
GcF(30,30,490)

