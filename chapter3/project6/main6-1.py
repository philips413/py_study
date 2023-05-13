import itertools

passwd_string = "01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1,4):
    to_attmpt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attmpt:
        passwd = ''.join(attempt)
        print(passwd)