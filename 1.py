import re

inp = input("Введите строку: ")

r = re.split('\s+', inp)

print(r[0],r[-1])