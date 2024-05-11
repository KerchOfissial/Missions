import re

inp = input("Введите строку: ")

pat = re.compile(r"\w+ма\w+")
pat2 = re.compile(r"\w+ро\w+")

r1 = re.findall(pat,inp)
r2 = re.findall(pat2, inp)
for i in r2:
    r1.append(i)
print(r1)