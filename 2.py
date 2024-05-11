import re

inp = input("Введите строку: ")

r = re.findall("[A-ZА-Я]{2,}", inp)

print(r)
