# list average

print("input size")
size = int(input())
numbers = []
sum = 0

for i in range(size):
    print("input number")
    number = int(input())
    numbers.append(number)
    sum += number
print(numbers)
avg = sum / size
print(f"average is {avg}")





















