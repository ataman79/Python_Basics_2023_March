from math import floor

record_sec = float(input())
distance_meters = float(input())
time_sec_meter = float(input())

time_for_distance = distance_meters * time_sec_meter
slowing_down = floor(distance_meters / 15) * 12.5
total_time = time_for_distance + slowing_down

diff = abs(total_time - record_sec)

if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")