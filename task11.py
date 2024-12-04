n = 174457
b = 0
while n < 174505:
    a = 2
    while a < n**0.5 + 1:
        if n % a == 0:
            b += 1
            a += 1
        if b < 2:
            print(n, a, n/a)
        b = 0
    n+=1
