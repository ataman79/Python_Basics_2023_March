city = input()
sell_ammount = float(input())
comission = -1


if city == "Sofia":
    if 0 <= sell_ammount <= 500:
        comission = 0.05

    elif  500 < sell_ammount <= 1000:
        comission = 0.07

    elif 1000 < sell_ammount <= 10000:
        comission = 0.08

    elif sell_ammount > 10000:
        comission = 0.12

elif city == "Varna":
    if 0 <= sell_ammount <= 500:
        comission = 0.045

    elif  500 < sell_ammount <= 1000:
        comission = 0.075

    elif 1000 < sell_ammount <= 10000:
        comission = 0.1

    elif sell_ammount > 10000:
        comission = 0.13


elif city == "Plovdiv":
    if 0 <= sell_ammount <= 500:
        comission = 0.055

    elif  500 < sell_ammount <= 1000:
        comission = 0.08

    elif 1000 < sell_ammount <= 10000:
        comission = 0.12

    elif sell_ammount > 10000:
        comission = 0.145

if comission >= 0:
    print(f"{sell_ammount * comission:.2f}")

else:
    print("error")