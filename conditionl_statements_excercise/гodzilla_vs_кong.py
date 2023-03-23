film_budget = float(input())
statisti_qty = int(input())
cloth_price_per_statist = float(input())

decor_sum = film_budget * 0.1
cloth_sum = statisti_qty * cloth_price_per_statist


if statisti_qty > 150:
    cloth_sum = cloth_sum - cloth_sum * 0.1

total_film_sum = decor_sum + cloth_sum

diff = abs(film_budget - total_film_sum)

if total_film_sum > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")

elif total_film_sum <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")