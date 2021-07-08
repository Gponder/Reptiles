c = chr(10084)
b = chr(12643)
key = 5
isHart = False

# 多线程可能出问题
for i in range(0, 14):
    if i < 3:
        x1 = i
        x = 4-x1*2
        y = 5+x1*4
    for j in range(0, 29):
        if not isHart:
            print(b, end='')
            x = x - 1
            if x < 0:
                isHart = True
        if isHart:
            print(c, end='')
            y = y - 1
            if y < 0:
                isHart = False
    print(i)

for i in range(0, 50000):
    c = chr(i)
    print(c, end='')
    if 'ㅣ' == c:
        print(i)
    if i % 100 == 0:
        print(i/100)
print(chr(10084))
