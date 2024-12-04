x = 1
while x < 2031:
    a = 3**100 - x
    b = 0
    while a > 0:
        a = a // 3
        if a % 3 == 0:
            b += 1
    if b == 2:
        print(a)
        break
    x += 1