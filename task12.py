n = 300000000
d = 2
b = 0
l = 0
while l < 6:
    while d < n**0.5:
        if n % d == 0:
            b += 1
            if b == 5:
                l += 1
                print(n, n/d)
        d+=1