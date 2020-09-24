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
