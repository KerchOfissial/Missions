import re

inp = input("Введите строку с датой(-ами): ")

dat = re.split('\d\d.\d\d.\d\d\s', inp)

print(dat)
