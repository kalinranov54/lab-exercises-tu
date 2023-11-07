# chete spisuk i premahva otricatelnite chisla

print("input size")
size = int(input())
numbers = []

for i in range(size):
    print("input number")
    number = int(input())
    numbers.append(number)
print(numbers)
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] < 0:
        numbers.pop(i)
print(numbers)
