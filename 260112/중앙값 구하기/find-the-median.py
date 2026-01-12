a, b, c = map(int, input().split())

if a>=b:
    if b>=c:
        print(b)
    else:   # c>b
        if a>=c:
            print(c)
        else:
            print(a)
else:   # b>a
    if a>=c:
        print(a)
    else:   # c>a
        if b>=c:
            print(c)
        else:
            print(b)