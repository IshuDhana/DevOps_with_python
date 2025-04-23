#creating integer variable and string variables
x = 5
Y = "DevOps with Python"
z = 'Language Python'
print (x)
print(Y)
print(z)

# casting variable 
a = str(3)
b = int(3)
c = float(3)

print(a,b,c)

#identifying type of variables
print(type(x))
print(type(Y))
print(type(a))
print(type(b))
print(type(c))
print(type(z))


#assigning variables
myvar = "DevOps"
MYVAR = "DevOps"
MyVar = "DevOps"
my_Var = "DevOps"
My_var = "DevOps"
_my_var = "DevOps"
my_var = "DevOps"
my_var2 = "DevOps"

print(myvar,
MYVAR,
MyVar,
my_Var,
My_var,
_my_var,
my_var,my_var2)

# should not use 
# 2myvar = "John"
#my-var = "John"
#my var = "John"

#declaring multiple variables at a time
p, q, r = "orange", "apple", "mango"
print(p,q,r)
print(p)
print(q)
print(r)

fruit = ["orange", "apple", "mango"]
p, q, r = fruit
print(p)
print(q)
print(r)


#merging strings
m = "DevOps"
n = "with"
o = "Python"
print(m,n,o)
print(m+n+o)
print(m+" "+n+" "+o)