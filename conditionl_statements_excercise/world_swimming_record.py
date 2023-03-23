from math import floor

record_sec = float(input())
distance_meters = float(input())
time_sec_meter = float(input())

time_for_distance = distance_meters * time_sec_meter
slowing_down = floor(distance_meters / 15) * 12.5
total_time = time_for_distance + slowing_down

diff = total_time - record_sec

if record_sec < total_time:
    print(f"No, he failed! He was {diff} seconds slower.")

elif record_sec > total_time:
    print(f"Yes, he succeeded! The new world record is {diff} seconds.")