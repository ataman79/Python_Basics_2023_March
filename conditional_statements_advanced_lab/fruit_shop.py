fruit = input().lower()
weekday = input()
quantity = float(input())
correct_data = True
price = 0

if weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" or \
        weekday == "Friday":

    if fruit == "banana":
        price = quantity * 2.50

    elif fruit == "apple":
        price = quantity * 1.20

    elif fruit == "orange":
        price = quantity * 0.85

    elif fruit == "grapefruit":
        price = quantity * 1.45

    elif fruit == "kiwi":
        price = quantity * 2.70

    elif fruit == "pineapple":
        price = quantity * 5.50

    elif fruit == "grapes":
        price = quantity * 3.85

    else:
        correct_data = False

elif weekday == "Saturday" or weekday == "Sunday":
    if fruit == "banana":
        price = quantity * 2.70

    elif fruit == "apple":
        price = quantity * 1.25

    elif fruit == "orange":
        price = quantity * 0.90

    elif fruit == "grapefruit":
        price = quantity * 1.60

    elif fruit == "kiwi":
        price = quantity * 3.00

    elif fruit == "pineapple":
        price = quantity * 5.60

    elif fruit == "grapes":
        price = quantity * 4.20

    else:
        correct_data = False

else:
    correct_data = False

if correct_data:
    print(f"{price:.2f}")

else:
    print("error")