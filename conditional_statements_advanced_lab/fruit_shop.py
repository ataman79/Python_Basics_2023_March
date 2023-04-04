fruit = input().lower()
weekday = input()
quantity = float(input())
price = 0

if weekday != ("Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday"
               or weekday == "Friday") or fruit != "banana":
    price = quantity * 2.50
    print(f"{price: .2f}")
else:
    print("error")
