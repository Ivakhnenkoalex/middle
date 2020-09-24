def ft_pow(num, s):
    result = 1
    s2 = 0
    while s2 < s:
        s2 += 1
        result *= num
    return result


def ft_len_num(a):
    b = 0
    if a > 0:
        while a >= 1:
            b = b + 1
            a = a / 10
    if a == 0:
        b = 0
    if a < 0:
        while a <= -1:
            b = b + 1
            a = a / 10
    return b


def ft_rev_bin_num(a):
    c = ft_len_num(a)
    k = 0
    for i in range(c):
        k += a % 10 + ft_pow(2, i)
        a //= 10
    return k
