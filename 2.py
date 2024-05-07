import re

while True:
    pot = input("Введите почту: ")
    pat = re.compile(r"\w{5,}@\w*mail\.\w{2,3}")
    r = re.findall(pat,pot)
    print(r)
    if r == []:
        print("Почта введена неправильно!")
        continue
    if r != []:
        print("Почта введена верно!")
        break
