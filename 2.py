import re

inp = input("Введите строку с датой(-ами): ")

dat = re.findall('\d\d.\d\d.\d\d', inp)

print(dat)