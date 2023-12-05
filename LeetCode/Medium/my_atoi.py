def add_digit(n: int, c: str) -> int:
    return n * 10 + int(c)

def myAtoi(s: str) -> int:
    n = 0
    sign = 0
    signs = '+-'
    started = False     # determines wether the digits enumeration started or not

    for c in s:
        if (c == ' ' and started) or \
            (c == ' ' and sign != 0):
            break
        elif c == ' ':
            continue
        if not started and c.isdigit():
            started = True
        if (not c.isdigit() and c not in signs) or \
            (c in signs and sign != 0) or \
            (started and c in signs):
            break
        if c == '+':
            sign = 1
        elif c == '-':
            sign = -1
        if c.isdigit() and c not in signs:
            n = add_digit(n, c)

    if sign == 0:
        sign = 1
    val = n * sign
    if val < -2**31:
        return -2**31
    if val > 2**31 - 1:
        return 2**31 - 1
    return val
