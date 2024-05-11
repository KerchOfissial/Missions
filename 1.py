import re

inp = input("Введите строку: ")
pat = re.compile(r"\w+-\w+")

r = re.findall(pat, inp)

print(r)
