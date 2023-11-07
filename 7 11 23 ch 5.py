# zad 1
print("input size")
size = int(input())
numbers = []

for i in range(size):
    print("input number")
    number = int(input())
    numbers.append(number)
print(numbers)
numbers.sort()
smallNum = numbers[0]
biggestNum = numbers[size - 1]
print(f"smallest is {smallNum}")
print(f"biggest is {biggestNum}")