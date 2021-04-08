def outer_func(a, b):
    def inner_func(c, d):
        return c+d
    return inner_func(a, b)

result = outer_func(5, 10)
print(result)
