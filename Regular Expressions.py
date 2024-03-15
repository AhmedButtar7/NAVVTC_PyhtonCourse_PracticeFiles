import re

txt = "The rain in Spain is happening in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("ai", txt)
print(x, y)

print(re.findall("Potuagl", txt))
z = re.search('\s', txt)
print("The First White Space is located in position : ", z.start())

x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

x = re.sub("\s", "9", txt)
print(x)

txt = "The rain is Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w", txt)
print(x.span())

x= re.search(r"\bS\w", txt)
print(x.string)

x= re.search(r"\bS\w+", txt)
print(x.group())