a = []
x = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(0, 8):
    temp_a = []
    for j in range(0, 8):
        temp_a.append(x[j])
        x[j] = x[j] * x[j]
    
    a.append(temp_a)    
print(a)    