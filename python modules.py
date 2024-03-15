import datetime
import math as m
import json

# Print date time using now
x = datetime.datetime.now()
print(x.strftime("%A, %B"))
print(x)
y = datetime.datetime(2004, 1, 1)
print(x - y)

# Use Math functions using math library
x = abs(-20)
print(x)
print(pow(2, 3))
print(m.sqrt(25))
print(m.pi)

# Use jason library
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])