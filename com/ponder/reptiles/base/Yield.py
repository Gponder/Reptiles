def fab(max_value):
    n, a, b = 0, 0, 1
    while n < max_value:
        yield b      # 使用 yield
        a, b = b, a + b  # 斐波那契数列
        n = n + 1  # 自增


for x in fab(5):
    print(x)
