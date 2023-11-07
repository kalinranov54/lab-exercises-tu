# zad 5
import random

print("input size")
size = int(input())
numbers = []
arrTwo = []
sum = 0

for i in range(size):
    print("input number")
    number = int(input())
    numbers.append(number)
    sum += number
print(numbers)
avg = sum / size
print(f"average is {avg}")

for i in range(size):
    number = random.randint(avg + 1, 100)
    arrTwo.append(number)
print(arrTwo)
