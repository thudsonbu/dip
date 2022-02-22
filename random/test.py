import re

x = re.search('^[0-9]*.[0-9]*$','.11a')

print(x)
print(x.span())