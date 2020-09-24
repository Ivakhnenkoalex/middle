def ft_len_num(a):
    b = 0
    if a > 0 :
        while a >= 1 :
            b = b + 1
            a = a / 10
    if a == 0:
        b = 0
    if a < 0:
        while a <= -1 :
            b = b + 1
            a = a / 10
    return b

def ft_multi_num(a):
    k = ft_len_num(a)
    c = 1
    if a > 0:
        while k > 0:
            k = k - 1
            c = c * (a % 10)
            a = a // 10
    elif a == 0:
        c = 0
    elif a < 0:
        a = -a
        while k > 0:
            k = k - 1
            c = c * (a % 10)
            a = a // 10
    return c

