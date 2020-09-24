def ft_bin_num(a):
    x = 1
    d = 0
    c = 0
    while a > 0:
        c = a % 16 * x
        if c >= 10:
            if c == 10:
                c = "A"
            elif c == 11:
                c = "B"
            elif c == 12:
                c = "C"
            elif c == 13:
                c = "D"
            elif c == 14:
                c = "E"
            else:
                c = "F"
            list(d)
            d = d +

        d = d + c
        x = x * 10
        a = a // 16
    return d


print(ft_bin_num(126))
