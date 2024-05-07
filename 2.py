import re

inp = input("Введите строку с датой(-ами): ")

dat = re.findall('\d{2}.\d{2}.\d{2}.', inp)
dat_2 = re.findall('\d{2}.\d{2}.\d{4}', inp)
for i in dat_2:
    dat.append(i)
    
print(dat)
