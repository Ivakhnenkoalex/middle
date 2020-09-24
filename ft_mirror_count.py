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

def ft_mirror_count(a):
    n = 0
    i = 1 ## Если не включаем 1 то i = 2
    while i <= a: ## Если не включаем а убрать =
        c = ft_rew_num(i)
        if c == i:
            n = n + 1
        i = i + 1
    return n


