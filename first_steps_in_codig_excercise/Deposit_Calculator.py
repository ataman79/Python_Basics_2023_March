deposit_sum = float(input())
deposit_term = int(input())
yield_percentage = float(input())
returned_sum = deposit_sum + deposit_term * ((deposit_sum * yield_percentage / 100) / 12)
print(returned_sum)