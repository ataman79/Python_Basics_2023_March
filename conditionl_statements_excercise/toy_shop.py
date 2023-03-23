holiday_price = float(input())
puzzle_qty = int(input())
dolls_qty = int(input())
bears_qty = int(input())
minion_qty = int(input())
trucks_qty = int(input())

final_toys_sum = 0

total_toys = puzzle_qty + dolls_qty + bears_qty + minion_qty + trucks_qty
toys_sum = puzzle_qty * 2.60 + dolls_qty * 3 + bears_qty * 4.10 + minion_qty * 8.20 + trucks_qty * 2

if total_toys >= 50:
    final_toys_sum = toys_sum - toys_sum * 0.25
else:
    final_toys_sum = toys_sum

rent = final_toys_sum * 0.1
profit = final_toys_sum - rent

# diff = abs(profit - holiday_price)    - прави абсолютна стойност
#if profit >= holiday_price:
#    print(f"Yes! {diff:.2f} lv left.")
#else:
#    print(f"Not enough money! {diff:.2f} lv needed.")

if profit >= holiday_price:
    print(f"Yes! {(profit - holiday_price):.2f} lv left.")

else:
    print(f"Not enough money! {(holiday_price - profit):.2f} lv needed.")

