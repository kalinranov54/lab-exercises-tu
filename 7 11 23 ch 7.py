# zad 3

print("input size")
size = int(input())
numbers = []
sum = 0

for i in range(size):
    print("input number")
    number = int(input())
    numbers.append(number)
    if i % 2 == 0:
        sum += number
print(numbers)
print(sum)
