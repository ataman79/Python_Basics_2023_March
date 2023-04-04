city = input()
sell_ammount = float(input())
comission = 0
FALSE_DATA = False

if city == "Sofia":
    if 0 <= sell_ammount <= 500:
        comission = sell_ammount * 0.05

    elif  500 < sell_ammount <= 1000:
        comission = sell_ammount * 0.07

    elif 1000 < sell_ammount <= 10000:
        comission = sell_ammount * 0.08

    elif sell_ammount > 10000:
        comission = sell_ammount * 0.12

    else:
        FALSE_DATA = True

elif city == "Varna":
    if 0 <= sell_ammount <= 500:
        comission = sell_ammount * 0.045

    elif  500 < sell_ammount <= 1000:
        comission = sell_ammount * 0.075

    elif 1000 < sell_ammount <= 10000:
        comission = sell_ammount * 0.1

    elif sell_ammount > 10000:
        comission = sell_ammount * 0.13

    else:
        FALSE_DATA = True

elif city == "Plovdiv":
    if 0 <= sell_ammount <= 500:
        comission = sell_ammount * 0.055

    elif  500 < sell_ammount <= 1000:
        comission = sell_ammount * 0.08

    elif 1000 < sell_ammount <= 10000:
        comission = sell_ammount * 0.12

    elif sell_ammount > 10000:
        comission = sell_ammount * 0.145

    else:
        FALSE_DATA = True

else:
    FALSE_DATA = True

if not  FALSE_DATA:
    print(f"{comission:.2f}")

else:
    print("error")