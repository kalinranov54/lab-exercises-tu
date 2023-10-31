# konvertor na valuti
# 0.85 ot dolari kum evro

print("write euro or usd")
a = input()
if a == "euro":
    print("input value")
    moneyBefore = float(input())
    moneyAfter = moneyBefore/0.85
    print(moneyAfter)

elif a == "usd":
    print("input value")
    moneyBefore = float(input())
    moneyAfter = moneyBefore * 0.85
    print(moneyAfter)

