import library_function

library_function.greeting("Mann")

print('-=-=-=-=-=-=-=-=-=-')

# datetime
import datetime

x = datetime.datetime.now()

print(x.year)

print('-=-=-=-=-=-=-=-=-=-')

# re
import re

txt = "Belajar Bahasa Pemrograman Python"
x = re.findall("Python", txt)

print(x)

print('-=-=-=-=-=-=-=-=-=-')

txt = "Belajar Bahasa Pemrograman Python"
x = re.split("\s", txt)

print('-=-=-=-=-=-=-=-=-=-')

txt = "Satu Dua Tiga Empat"
x = re.sub("Dua", "2", txt)

print(x)

import math

