def print_str() -> '返回值的类型注释,通常写返回值的类型 类似java中方法返回值类型 void,但是不验证 所以可以瞎jb写 ':
    """doc strings 文档 方法注释 也可以不写"""
    print('v')


# 方法块要空两行
# 类名驼峰 方法名下划线
print_str()
print(print_str.__annotations__)
