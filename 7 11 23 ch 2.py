#chete imena, izpisva broq imena, zapochvashti s A

print("input size")
size = int(input())
names = []
counter = 0

for i in range(size):
    print(f"input name {i+1}")
    name = input()
    for j in name:
        if j == 'A' or j == 'a':
            counter += 1
        break
    names.append(name)
print(names)
print(f"{counter} names start with a")
