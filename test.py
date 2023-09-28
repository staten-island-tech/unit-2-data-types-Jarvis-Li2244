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
# print(gcf(230,50))

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
# GcF(30,30,490)


def factors(z,x):
    while z <= x:
        if x % z == 0:
            print(z)
            z += 1
        else: 
            z += 1

# factors(1,74)

def factors(x):
    z = x
    while z > 0:
        if x % z == 0:
            print(z)
            z -= 1
        else: 
            z -= 1

x = True
y = False

def traffic(x, y):
    if type(x) == bool and type(y) == bool:
        print(not(x == y))
    else:
        print("Error, try again.")


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
# print(gcf(230,50))

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
# GcF(10,10,25)


def factors(z,x):
    while z <= x:
        if x % z == 0:
            print(z)
            z += 1
        else: 
            z += 1

# factors(1,1000)


factorx = []
factory = []

def actor(x):
    a = 1
    while a <= x:
        if x % a == 0:
            factorx.append(a)
            a += 1
        else: 
            a += 1

def actor2(y):
    b = 1
    while b <= y:
        if y % b == 0:
            factory.append(b)
            b += 1
        else: 
            b += 1

cf = []
# This is also used for GCF
def listing(x,y):
    actor(x)
    actor2(y)
    for x in factorx:
        for y in factory:
            if x == y:
                cf.append(x)
    print(cf)
    print(cf[-1]) #***
    print(cf[len(cf)-1]) #***
#*** These two lines perform the same action.

# for i in (anylist):
    # print(-i)
# prints all values in the list as negative.

def listin(x,y):
    actor(x)
    actor2(y)
    for i in factorx:
        if i in factory:
            cf.append(i)
    print(cf[-1])