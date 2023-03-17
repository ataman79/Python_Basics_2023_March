count_chicken = int(input())
count_fish = int(input())
count_veggy = int(input())

price_chicken = count_chicken * 10.35
price_fish = count_fish * 12.40
price_veggy = count_veggy * 8.15
total_price_menus = price_chicken + price_fish + price_veggy
price_desert = total_price_menus * 0.2

total_price_order = total_price_menus + price_desert + 2.5

print(total_price_order)