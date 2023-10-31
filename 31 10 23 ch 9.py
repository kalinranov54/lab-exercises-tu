# zad 6
input("input start num")
start = int(input())
input("input end num")
end = int(input())
num = start
while True:
    if num % 2 == 1:
        print(f"purvoto nechetno chislo v intervala e {num}")
        break
    else:
        num += 1
