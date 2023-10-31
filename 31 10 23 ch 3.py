print("input name")
name = input()
if len(name) > 0:
    if len(name.split()) == 2:
        print(name)
    else:
        print("not 2 words")
else:
    print("empty")

