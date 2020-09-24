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

def ft_null_count(a):
    k = ft_len_num(a)
    m = 0
    c = 0
    if a > 0:
        while k > 0:
            k = k - 1
            c = (a % 10)
            a = a // 10
            if c == 0:
                m = m + 1
    elif a == 0:
        c = 0
    elif a < 0:
        a = -a
        while k > 0:
            k = k - 1
            c = (a % 10)
            a = a // 10
            if c == 0:
                m = m + 1
    return m

