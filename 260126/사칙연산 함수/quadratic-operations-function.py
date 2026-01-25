a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calculator(a, o, c):
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '/':
        return a / c
    elif o == '*':
        return a * c
    else:
        return False

result = calculator(a, o, c)

if result:
    print(f"{a} {o} {c} = {result}")
else:
    print("False")