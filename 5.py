import re
while True:
    inp = input("Введите пароль: ")
    r = re.search('.{8,24}', inp)
    if r == None:
        print(f'{inp} - ненадёжный пароль!')
        continue
    else:
        r = re.search('[A-Z][a-z]', inp)
        if r == None:
            print(f'{inp} - ненадёжный пароль!')
            continue
        else:
            r = re.search('\d', inp)
            if r == None:
                print(f'{inp} - ненадёжный пароль!')
                continue
            else:
                r = re.search('[-_/?!@<>=+*]', inp)
                if r == None:
                    print(f'{inp} - ненадёжный пароль!')
                    continue
                else:
                    print("Пароль сохранён")
                    break
