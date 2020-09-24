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

def ft_max_num(a):
    k = ft_len_num(a)
    m = 0
    c = 0
    if a > 0:
        while k > 0:
            k = k - 1
            c = (a % 10)
            a = a // 10
            if c > m:
                m = c
    elif a == 0:
        c = 0
    elif a < 0:
        a = -a
        while k > 0:
            k = k - 1
            c = (a % 10)
            a = a // 10
            if c > m:
                m = c
    return m

def ft_second_max_num(a):
    c = ft_max_num(a)
    k = ft_len_num(a)
    x = 0
    b = 1
    l = a
    if a > 0:
        while k > 0:
            k = k - 1
            b = b + 1
            x = (a % 10)
            a = a // 10
            if x == c:
                z = k - b

    elif a < 0:
        a = -a
        while k > 0:
            k = k - 1
            b = b + 1
            x = (a % 10)
            a = a // 10
            if x == c:
                z = k - b
    if z == 0:
        l = l - c
    else:
        l = l - (c *( 10 ** z))
    return l

print(ft_second_max_num(132))




