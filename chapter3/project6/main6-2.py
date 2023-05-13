import itertools
import zipfile

passwd_string = "01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile("암호1234.zip")

for len in range(1,6) :
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd = passwd.encode())
            print(f"비밀번호는 {passwd} 입니다.")
            break
        except:
            pass

## jSy