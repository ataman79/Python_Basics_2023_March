lenght_cm = int(input())
wide_cm = int(input())
height_cm = int(input())
percent_occupied = float(input()) / 100

volume_cm = lenght_cm * wide_cm * height_cm
volume_l = volume_cm * 0.001

water_percent = 1 - percent_occupied
water_needed = volume_l * water_percent

print(water_needed)


