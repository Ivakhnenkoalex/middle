def ft_rew_num(a):
    p = 0
    k = 0
    if a == 0:
        return a
    elif a > 0:
        while a > 0:
            k = a % 10
            a = a // 10
            p = p * 10
            p = p + k
        return p
    elif a < 0:
        a = -a
        while a > 0:
            k = a % 10
            a = a // 10
            p = p * 10
            p = p + k
        return p
