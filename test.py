# naem_zala = float(input())
# tort_price = naem_zala * 0.2
# drink_price = tort_price - (tort_price * 0.45)
# animator_price = naem_zala / 3
# needed_sum = naem_zala + tort_price + drink_price + animator_price
# print(needed_sum)


btc_qnt = int(input())
yuan_qnt = float(input())
comission = float(input())
btc_change = btc_qnt * 1168
yuan_change_leva = (yuan_qnt * 0.15) * 1.76
total_leva = btc_change + yuan_change_leva
leva_to_eur = total_leva / 1.95
leva_to_eur_com = leva_to_eur * (comission / 100)
total_euro = leva_to_eur  - leva_to_eur_com
total_euro_rounded = round(total_euro, 2)
print(total_euro_rounded)
