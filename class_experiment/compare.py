a, b, c = 3, 4, 5
if a > b:
    if a > c:
        a = a+b
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
        print('ok')
