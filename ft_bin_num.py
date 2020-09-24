def ft_bin_num(a):
    x = 1
    d = 0
    while a > 0:
        d = d + a % 2 * x
        x = x * 10
        a //= 2
    return d
