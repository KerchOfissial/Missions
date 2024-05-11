import re

inp = input("Введите строку с тегами: ")

pat = re.compile(r"<\w+>\w+<\\\w+>")

r = re.findall(pat, inp)

word1 = ''
word2 = ''

for i in r:
    word1 = re.sub(r"<\w+>", "", i)
    word2 = re.sub(r"<\\\w+>", '', word1)
    print(word2)
