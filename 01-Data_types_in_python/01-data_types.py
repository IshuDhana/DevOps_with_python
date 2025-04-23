x = str("Hello world")
print(x)
print(type(x))

x = int(10)
print(x)
print(type(x))

x = int(-10)
print(x)
print(type(x))

x = float(10.25)
print(x)
print(type(x))

x = complex(10j)
print(x)
print(type(x))

x = list(("apples", "berry", "cherry"))
print(x)
print(type(x))

x = tuple(("apples", "berry", "cherry"))
print(x)
print(type(x))

x = range(6)
print(x)

x = dict(value = "DevOps", lang = "python")
print(x)

x = set(("tulip", "jasmin"))
print(x)

x = frozenset(("tulip", "rose"))
print(x)

x = bool(5)
print(x)

x = bytes(5)
print(x)

x = bytearray(5)
print(x)

x = memoryview(bytes(5))
print(x)


#casting for int, float, string

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3")
print(x,y,z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2")
print(x,y,z,w)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)