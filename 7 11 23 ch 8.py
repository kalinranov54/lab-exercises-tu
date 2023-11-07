# zad 4

print("input size")
size = int(input())
numbers = []
numbersQ = []

for i in range(size):
    print("input number")
    number = int(input())
    numberQ = number * number
    numbers.append(number)
    numbersQ.append(numberQ)
print(numbers)
print(numbersQ)

