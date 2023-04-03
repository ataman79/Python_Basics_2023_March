from math import ceil

series_name = input()
series_lenght = int(input())
break_lenght = int(input())

lunch_lenght = break_lenght * 1 / 8
rest_lenght = break_lenght * 1 / 4
remain_time = break_lenght - lunch_lenght - rest_lenght


if remain_time >= series_lenght:
    print(f"You have enough time to watch {series_name} and left with {ceil(remain_time - series_lenght)} minutes free time.")

else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(series_lenght - remain_time)} more minutes.")