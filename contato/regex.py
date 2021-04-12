import re

a = r"^((\+\d{1,3})?\(\d{2,3}\))?\d{4,5}-\d{4}$" 


print(bool(re.match(a, '88756-903gfg')))

pd = r"\(\d{2}\)\d{4}\-\d{4}"
teste = r"\d{2}\-\d{2}"

while 1:
    print(bool(re.match(teste, input())))