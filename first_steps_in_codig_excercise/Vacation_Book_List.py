pages = int(input())
pages_per_hour = int(input())
days = int(input())
total_read_hours = pages // pages_per_hour
needed_hours_per_day = total_read_hours / days


print(needed_hours_per_day)
