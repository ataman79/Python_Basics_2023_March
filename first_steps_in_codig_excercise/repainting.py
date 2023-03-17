nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours = int(input())
sum_nylon_needed = (nylon_needed + 2) * 1.50
sum_paint_needed = (paint_needed + paint_needed * (10 / 100)) * 14.50
sum_thinner_needed = thinner_needed * 5.00
sum_torbichki = 0.40
total_material_sum = sum_nylon_needed + sum_paint_needed + sum_thinner_needed + sum_torbichki
sum_workers_per_hour = total_material_sum * 0.3
total_workers_sum = sum_workers_per_hour * hours

print(total_workers_sum + total_material_sum)
