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



