lenght_cm = int(input())
wide_cm = int(input())
height_cm = int(input())
percent_occupied = float(input()) / 100

volume_cm = lenght_cm * wide_cm * height_cm
volume_l = volume_cm * 0.001

water_percent = 1 - percent_occupied
water_needed = volume_l * water_percent

print(water_needed)




# # Read in the dimensions and percentage from the console
# length = int(input())
# width = int(input())
# height = int(input())
# percentage = float(input())
#
# # Calculate the volume of the aquarium in cubic centimeters
# volume_cm3 = length * width * height
#
# # Calculate the volume of the non-water components in cubic centimeters
# non_water_volume_cm3 = percentage/100 * volume_cm3
#
# # Calculate the volume of water in cubic centimeters
# water_volume_cm3 = volume_cm3 - non_water_volume_cm3
#
# # Convert the volume of water to liters
# water_volume_l = water_volume_cm3/1000
#
# # Output the result to the console
# print(water_volume_l)
