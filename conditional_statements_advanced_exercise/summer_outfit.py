degree = int(input())
day_time = input()

outfit = ""
shoes = ""

if day_time == "Morning" and 10 <= degree <= 18:
    outfit = "Sweatshirt"
    shoes = "Sneakers"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

elif day_time == "Afternoon" and 10 <= degree <= 18:
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

elif day_time == "Evening" and 10 <= degree <= 18:
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

if day_time == "Morning" and 18 < degree <= 24:
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

elif day_time == "Afternoon" and 18 < degree <= 24:
    outfit = "T-Shirt"
    shoes = "Sandals"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

elif day_time == "Evening" and 18 < degree <= 24:
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

if day_time == "Morning" and degree > 25:
    outfit = "T-Shirt"
    shoes = "Sandals"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

elif day_time == "Afternoon" and degree > 25:
    outfit = "Swim Suit"
    shoes = "Barefoot"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

elif day_time == "Evening" and degree > 25:
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

