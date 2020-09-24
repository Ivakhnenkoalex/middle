def ft_bin_num(a):
    x = 1
    d = 0
    while a > 0:
        d = d + a % 8 * x
        x = x * 10
        a = a // 8
    return d

print(ft_bin_num(32))