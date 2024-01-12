
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on 01/12/2024  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


##### 4.1. if Statements #####

# Perhaps the most well-known statement type is the if statement. For example:

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# There can be zero or more elif parts, and the else part is optional. The 
# keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive 
# indentation. An if … elif … elif … sequence is a substitute for the switch or 
# case statements found in other languages.

# If you’re comparing the same value to several constants, or checking for 
# specific types or attributes, you may also find the match statement useful. 
# For more details see match Statements.


##### 4.2. for Statements #####

# The for statement in Python differs a bit from what you may be used to in C or 
# Pascal. Rather than always iterating over an arithmetic progression of numbers 
# (like in Pascal), or giving the user the ability to define both the iteration 
# step and halting condition (as C), Python’s for statement iterates over the 
# items of any sequence (a list or a string), in the order that they appear 
# in the sequence. For example (no pun intended):

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Code that modifies a collection while iterating over that same collection can be 
# tricky to get right. Instead, it is usually more straight-forward to loop over 
# a copy of the collection or to create a new collection:

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# alternative:

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


##### 4.3. The range() Function #####

# If you do need to iterate over a sequence of numbers, the built-in function 
# range() 
# comes in handy. It generates arithmetic progressions:

for i in range(5):  # starts to count from 0 to 4
    print(i)

# The given end point is never part of the generated sequence; range(10) 
# generates 10 values, the legal indices for items of a sequence of length 10. 
# It is possible to let the range start at another number, or to specify a 
# different increment (even negative; sometimes this is called the ‘step’):

list(range(5, 10))  # counts from 5 to 9

list(range(0, 10, 3))  # counts from 0 to 9 with step 3

list(range(-10, -100, -30))  # counts from -1- to -10, step -30

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# In most such cases, however, it is convenient to use the enumerate() function, 
# see Looping Techniques.

# A strange thing happens if you just print a range:

range(10)

# In many ways the object returned by range() behaves as if it is a list, but 
# in fact it isn’t. It is an object which returns the successive items of the 
# desired sequence when you iterate over it, but it doesn’t really make the list, 
# thus saving space.

# We say such an object is iterable, that is, suitable as a target for functions 
# and constructs that expect something from which they can obtain successive 
# items until the supply is exhausted. We have seen that the for statement is 
# such a construct, while an example of a function that takes an iterable 
# is sum():

sum(range(4))  # 0 + 1 + 2 + 3

# Later we will see more functions that return iterables and take iterables as 
# arguments. In chapter Data Structures, we will discuss in more detail about 
# list()


##### 4.4. break and continue Statements, and else Clauses on Loops #####

# The break statement breaks out of the innermost enclosing for or while loop.

# A for or while loop can include an else clause.

# In a for loop, the else clause is executed after the loop reaches its 
# final iteration.

# In a while loop, it’s executed after the loop’s condition becomes false.

# In either kind of loop, the else clause is not executed if the loop 
# was terminated by a break.

# This is exemplified in the following for loop, which searches for 
# prime numbers:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# (Yes, this is the correct code. Look closely: the else clause belongs to the 
# for loop, not the if statement.)

# When used with a loop, the else clause has more in common with the else clause 
# of a try statement than it does with that of if statements: a try statement’s 
# else clause runs when no exception occurs, and a loop’s else clause runs when 
# no break occurs. For more on the try statement and exceptions, see 
# Handling Exceptions.

# The continue statement, also borrowed from C, continues with the next iteration 
# of the loop:

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


##### 4.5 pass Statements #####

# The pass statement does nothing. It can be used when a statement is required 
# syntactically but the program requires no action. For example:

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# This is commonly used for creating minimal classes:

class MyEmptyClass:
    pass

# Another place pass can be used is as a place-holder for a function or 
# conditional body when you are working on new code, allowing you to keep 
# thinking at a more abstract level. The pass is silently ignored:

def initlog(*args):
    pass   # Remember to implement this!


##### 4.6. match Statements #####

# A match statement takes an expression and compares its value to successive 
# patterns given as one or more case blocks. This is superficially similar to 
# a switch statement in C, Java or JavaScript (and many other languages), but 
# it’s more similar to pattern matching in languages like Rust or Haskell. 
# Only the first pattern that matches gets executed and it can also extract 
# components (sequence elements or object attributes) from the value into 
# variables.

# The simplest form compares a subject value against one or more literals:

def http_error(status): # defines a function, argument is status
    match status:  #  defines some status value (cases) in order to say something
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

http_error(400)

# Note the last block: the “variable name” _ acts as a wildcard and never fails 
# to match. If no case matches, none of the branches is executed.

# You can combine several literals in a single pattern using | (“or”):

def http_error(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"

http_error(403)

# Patterns can look like unpacking assignments, and can be used to bind variables:

# point is an (x, y) tuple
# for example:
point=(4, 8)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")  # in this case we assign 4 to x and 8 to y
    case _:
        raise ValueError("Not a point")

# Study that one carefully! The first pattern has two literals, and can be thought 
# of as an extension of the literal pattern shown above. But the next two patterns 
# combine a literal and a variable, and the variable binds a value from the 
# subject (point). The fourth pattern captures two values, which makes it 
# conceptually similar to the unpacking assignment (x, y) = point.

##### 4.6. match Statements - to be continued #####


##### let's study Class #####
##### 9.3.2. Class Objects #####

# Class objects support two kinds of operations: attribute references and 
# instantiation.

# Attribute references use the standard syntax used for all attribute references in 
# Python: obj.name. Valid attribute names are all the names that were in the 
# class’s namespace when the class object was created. So, if the class definition 
# looked like this:

class MyClass:
    """A simple example class"""  # valid attribute MyClass.__doc__
    i = 12345  # valid attribute MyClass.i
    def f(self):   " valid attribute MyClass.f
        return 'hello world'

MyClass.i
MyClass.f(1)
MyClass.f

# then MyClass.i and MyClass.f are valid attribute references, returning an integer 
# and a function object, respectively. Class attributes can also be assigned to, 
# so you can change the value of MyClass.i by assignment. 
# __doc__ is also a valid attribute, returning the docstring belonging 
# to the class: "A simple example class".

MyClass.i = 345
MyClass.i

MyClass.__doc__  # return 'A simple example class'

# Class instantiation uses function notation. Just pretend that the class object is 
# a parameterless function that returns a new instance of the class. For example 
# (assuming the above class):

x = MyClass()

# creates a new instance of the class and assigns this object to the local 
# variable x.

# The instantiation operation (“calling” a class object) creates an empty object. 
# Many classes like to create objects with instances customized to a specific 
# initial state. Therefore a class may define a special method named 
# __init__(), 
# like this:

def __init__(self):
    self.data = []

# When a class defines an __init__() method, class instantiation automatically 
# invokes __init__() for the newly created class instance. So in this example, a new, 
# initialized instance can be obtained by:

x = MyClass()

# Of course, the __init__() method may have arguments for greater flexibility. 
# In that case, arguments given to the class instantiation operator are 
# passed on to __init__(). For example,

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)  # these arguments 3.0 and -4.5 are passed on to __init__()
x.r, x.i   # it is like self.r but we created instantiation


##### 4.6. match Statements - continue #####

# If you are using classes to structure your data you can use the class name followed 
# by an argument list resembling a constructor, but with the ability to capture 
# attributes into variables:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

temp = Point(0, 0)
temp.x
temp.y

temp2 = Point(4, 6)
temp2.x
temp2.y

# in this way it is possible to create new objects with different point values

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(temp)
where_is(temp2)


##### let's study about the special attribute __match_args__ #####
##### https://earthly.dev/blog/structural-pattern-matching-python/ #####

# Python classes do not have a natural ordering of their attributes, we 
# need to specify the order of the attributes using the 
# __match_args__ attribute before we can use the positional 
# arguments in the patterns.

class Post:
    __match_args__ = ("post_id", "userId", "title", "body")
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.title = title
        self.body = body
        self.post_id = id

# The __match_args__ allows us to order the attributes based on our preference.

    # - In the case above, the first argument in the pattern will match against 
    #   the equivalent first value in the __match__args.

    # - The post_id will be the first positional argument, the userId will be the 
    #   second while the title and body will be the third and fourth positional 
    #   arguments respectively.

# If positional patterns are present in a class, they are converted to keyword 
# patterns based on the arrangement in the __match_args__ attribute.


##### Matching the structure of objects ######
##### https://mathspp.com/blog/pydonts/structural-pattern-matching-tutorial #####

# Structural pattern matching can also be used to match the structure of class 
# instances. Let us recover the Point2D class I have used as an example in a 
# couple of posts, in particular the Pydon't about __str__ and __repr__:

class Point2D:
    """A class to represent points in a 2D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Provide a good-looking representation of the object."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Provide an unambiguous way of rebuilding this object."""
        return f"Point2D({repr(self.x)}, {repr(self.y)})"

# Imagine we now want to write a little function that takes a Point2D and writes a 
# little description of where the point lies. We can use pattern matching to 
# capture the values of the x and y attributes and, what is more, we can use short 
# if statements to help narrow down the type of matches we want to succeed!

# Take a look at the following:

def describe_point(point):
    """Write a human-readable description of the point position."""

    match point:
        case Point2D(x=0, y=0):
            desc = "at the origin"
        case Point2D(x=0, y=y):
            desc = f"in the vertical axis, at y = {y}"
        case Point2D(x=x, y=0):
            desc = f"in the horizontal axis, at x = {x}"
        case Point2D(x=x, y=y) if x == y:
            desc = f"along the x = y line, with x = y = {x}"
        case Point2D(x=x, y=y) if x == -y:
            desc = f"along the x = -y line, with x = {x} and y = {y}"
        case Point2D(x=x, y=y):
            desc = f"at {point}"

    return "The point is " + desc

# Prints "The point is at the origin"
print(describe_point(Point2D(0, 0)))

# Prints "The point is in the horizontal axis, at x = 3"
print(describe_point(Point2D(3, 0)))

# Prints "# The point is along the x = -y line, with x = 3 and y = -3"
print(describe_point(Point2D(3, -3)))

# Prints "# The point is at (1, 2)"
print(describe_point(Point2D(1, 2)))


##### __match_args__ #####

# Now, I don't know if you noticed, but didn't all the x= and y= in the code snippet 
# above annoy you? Every time I wrote a new pattern for a Point2D instance, I had to 
# specify what argument was x and what was y. For classes where this order is not 
# arbitrary, we can use __match_args__ to tell Python how we would like match 
# to match the attributes of our object.

# Here is a shorter version of the example above, making use of __match_args__ 
# to let Python know the order in which arguments to Point2D should match:

class Point2D:
    """A class to represent points in a 2D space."""

    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point(point):
    """Write a human-readable description of the point position."""

    match point:
        case Point2D(0, 0):
            desc = "at the origin"
        case Point2D(0, y):
            desc = f"in the vertical axis, at y = {y}"
        case Point2D(x, 0):
            desc = f"in the horizontal axis, at x = {x}"
        case Point2D(x, y):
            desc = f"at {point}"

    return "The point is " + desc

# Prints "The point is at the origin"
print(describe_point(Point2D(0, 0)))

# Prints "The point is in the horizontal axis, at x = 3"
print(describe_point(Point2D(3, 0)))

# Prints "# The point is at (1, 2)"
print(describe_point(Point2D(1, 2)))


##### 4.6. match Statements - continue #####

# You can use positional parameters with some builtin classes that provide an 
# ordering for their attributes (e.g. dataclasses). You can also define a specific 
# position for attributes in patterns by setting the __match_args__ special attribute 
# in your classes. If it’s set to (“x”, “y”), the following patterns are all 
# equivalent (and all bind the y attribute to the var variable):

Point(1, var) 
Point(1, y=var) 
Point(x=1, y=var) 
Point(y=var, x=1) 

# A recommended way to read patterns is to look at them as an extended form of what 
# you would put on the left of an assignment, to understand which variables would 
# be set to what. Only the standalone names (like var above) are assigned to by a 
# match statement. Dotted names (like foo.bar), attribute names (the x= and y= above) 
# or class names (recognized by the “(…)” next to them like Point above) are never 
# assigned to.

# Patterns can be arbitrarily nested. For example, if we have a short list of Points, 
# with __match_args__ added, we could match it like this:

class Point:
    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def where_is(points):
  match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

##### code above not clear #####

# We can add an if clause to a pattern, known as a “guard”. If the guard is false, 
# match goes on to try the next case block. Note that value capture happens before 
# the guard is evaluated:

point = Point(3, 3)

match point:
    case Point(x, y) if x == y:    # for Point(3, 3) is True
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

# Several other key features of this statement:

    # - Like unpacking assignments, tuple and list patterns have exactly the same 
    #   meaning and actually match arbitrary sequences. An important exception is  
    #   that they don’t match iterators or strings.

    # - Sequence patterns support extended unpacking: [x, y, *rest] and (x, y, *rest) 
    #   work similar to unpacking assignments. The name after * may also be _, 
    #   so (x, y, *_) matches a sequence of at least two items without binding the 
    #   remaining items.

    # - Mapping patterns: {"bandwidth": b, "latency": l} captures the "bandwidth" 
    #   and "latency" values from a dictionary. Unlike sequence patterns, extra keys 
    #   are ignored. An unpacking like **rest is also supported. (But **_ would be 
    #   redundant, so it is not allowed.)

    # - Subpatterns may be captured using the as keyword:
        case (Point(x1, y1), Point(x2, y2) as p2): ...
    #   will capture the second element of the input as p2 (as long as the input is a 
    #   sequence of two points)

    # - Most literals are compared by equality, however the singletons True, False 
    #   and None are compared by identity.

    # - Patterns may use named constants. These must be dotted names to prevent 
    #   them from being interpreted as capture variable:

        from enum import Enum
        class Color(Enum):
            RED = 'red'
            GREEN = 'green'
            BLUE = 'blue'

        color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

        match color:
            case Color.RED:
                print("I see red!")
            case Color.GREEN:
                print("Grass is green")
            case Color.BLUE:
                print("I'm feeling the blues :(")

    #   For a more detailed explanation and additional examples, you can look into 
    #   PEP 636 which is written in a tutorial format.



