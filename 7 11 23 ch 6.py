# zad 2

print("input size")
size = int(input())
numbers = []
counter = 0

for i in range(size):
    print("input number")
    number = int(input())
    if number % 3 == 0:
        counter += 1
    numbers.append(number)
print(numbers)
print(counter)
