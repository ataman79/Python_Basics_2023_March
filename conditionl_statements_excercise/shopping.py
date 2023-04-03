budget = float(input())
videocards = int(input())
cpu = int(input())
ram = int(input())

sum_videocards = videocards * 250
cpu_price = sum_videocards * 0.35
sum_cpu = cpu_price * cpu
ram_price = sum_videocards * 0.1
sum_ram  =ram_price * ram

total_sum = sum_videocards + sum_cpu + sum_ram

if videocards > cpu:
    total_sum = sum_videocards + sum_cpu + sum_ram - (sum_videocards + sum_cpu + sum_ram) * 0.15

if budget >= total_sum:
    print(f"You have {budget - total_sum:.2f} leva left!")

else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")

# if budget >= total_sum:
#     if videocards > cpu:
#         total_sum = sum_videocards + sum_cpu + sum_ram - (sum_videocards + sum_cpu + sum_ram) * 0.15
#         print(f"You have {budget - total_sum:.2f} leva left!")
#     else:
#         total_sum = sum_videocards + sum_cpu + sum_ram
#         print(f"You have {budget - total_sum:.2f} leva left!")
#
# else:
#     if videocards > cpu:
#         total_sum = sum_videocards + sum_cpu + sum_ram - (sum_videocards + sum_cpu + sum_ram) * 0.15
#         print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")
#     else:
#         total_sum = sum_videocards + sum_cpu + sum_ram
#         print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")


