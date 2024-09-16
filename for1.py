import math
n = int(input("n = "))
total_sum = 0
current_sum = 0

for i in range(1, n + 1):
    current_sum = current_sum + math.sin(i)
    total_sum = total_sum + 1/current_sum

print(f"{n}= {total_sum}")