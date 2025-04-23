# declaring a function
def greet(Text):
    return f"Hello, {Text}!"

message = greet("ishu")
print(message)

#A function is a block of code which only runs when it is called.

#You can pass data, known as parameters, into a function.

#function can return data as a result.
def sample_function():
    print("Hello function")

sample_function()

def sample_function_with_arg(name):
    print(name +"!!!")

sample_function_with_arg("devops")
sample_function_with_arg("with")
sample_function_with_arg("python")

def sample_function_with_arg2(name, value):
    print(name +"!!!"+value)

sample_function_with_arg2("devops", "@")
sample_function_with_arg2("with", "@")
sample_function_with_arg2("python", "@")



def sample_function_list(*kids):
    print("Hello function"+" " +kids[2])

sample_function_list("Tim", "Tom", "Jerry")

def my_function_three_para(child3, child2, child1):
  print("The youngest child is " + child3)

my_function_three_para(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function_multi_star(**kid):
  print("His last name is " + kid["lname"])

my_function_multi_star(fname = "Tobias", lname = "Refsnes")

def my_country(country = "India"):
   print("I am from" + country)

my_country("sweden")
my_country("India")
my_country()

def my_country(country = "India"):
   for i in country:
        print("I am from" + i)

country = ["India", "sweden"]
my_country(country)

def my_function_cal(x):
    return 5 * x

print(my_function_cal(3))

#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

#You can combine the two argument types in the same function.

#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5,6, c = 7, d = 8)

#To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
  print(x)

my_function(x = 3)

#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

#To specify that a function can have only positional arguments, add , / after the arguments:

def my_function(x, /):
  print(x)

my_function(3)