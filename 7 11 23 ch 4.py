# sortira v nizhodqsht red

print("input size")
size = int(input())
numbers = []

for i in range(size):
    print("input number")
    number = int(input())
    numbers.append(number)
print(numbers)

numbers.sort(reverse=True)
print(numbers)

