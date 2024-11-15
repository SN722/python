if 5 > 2:
  print("Five is greater than two!")
  
x = 2
y = 5
print(x)
print(y)


# casting methods
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

# finding type method
print(type(x))
print(type(y))

# python allows to assign multiple variables in a single line 

x, y, z = "one","two","three"
print(x)
print(y)
print(z) 

# and also same value to multiple variables

a = b = c = "same"
print(a,b,c)

# unpack a collection
fruits = ("Apple","Banana","Mango")
x, y, z = fruits
print(x,y,z)
print(fruits)

# Numbers

# converting number type to another type
s = float(1)
u = int(2.8)
v = complex(1)

print(s)
print(u)
print(v)

print(type(s))
print(type(u))
print(type(v))

# in python we cant concat the number and string but its possible by using format string
# format string

rate = 50
txt = f"the rate of Apple is {rate} per kg"
print(txt)

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

rate1 = 30
txt1 = f"Oranges are rupees {rate1:.2f} per kg"
print(txt1)

# and it will done mathematics operations also
hi = f"the addition of 10 + 30 is:{10 + 30}"
print(hi)