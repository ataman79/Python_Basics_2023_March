yield_tax = int(input())
kecove = yield_tax - (yield_tax * 0.4)
equip = kecove - (kecove * 0.2)
ball = equip * 1 / 4
acc = ball * 1 / 5
total_equip_price = yield_tax + kecove + equip + ball + acc

print(total_equip_price)