c = 1
x = ""
s = [0, ""]
a = input("Введите:")
for i in range(len(a)):
    x = a[i]
    if a[i] == x:
        c += 1
    else:
        s.append(c)
