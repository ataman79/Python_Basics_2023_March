current_hour = int(input())
current_minutes = int(input())

total_time_minutes = current_hour * 60 + current_minutes + 15

hours = total_time_minutes // 60
minutes = total_time_minutes % 60

#if hours > 23:
if hours == 24:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")

else:
    print(f"{hours}:{minutes}")

