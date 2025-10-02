numbers = [156, 124, 200, 23, 64]


n = len(numbers)

for i in range(len(numbers)):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)