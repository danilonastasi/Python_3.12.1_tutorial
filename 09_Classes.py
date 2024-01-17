
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on _________ -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


##### 9. Classes #####

# Classes provide a means of bundling data and functionality together. Creating 
# a new class creates a new type of object, allowing new instances of that type 
# to be made. Each class instance can have attributes attached to it for maintaining 
# its state. Class instances can also have methods (defined by its class) for 
# modifying its state.
# Python classes provide all the standard features of Object Oriented Programming: 
# the class inheritance mechanism allows multiple base classes, a derived class 
# can override any methods of its base class or classes, and a method can call the 
# method of a base class with the same name. 


##### 9.1. A Word About Names and Objects #####

# Objects have individuality, and multiple names (in multiple scopes) can be bound 
# to the same object. This is known as aliasing in other languages. 


##### 9.2. Python Scopes and Namespaces #####

# Before introducing classes, I first have to tell you something about Python’s 
# scope rules. Class definitions play some neat tricks with namespaces, and you 
# need to know how scopes and namespaces work to fully understand what’s going on. 
# Incidentally, knowledge about this subject is useful for any advanced Python 
# programmer.

# Let’s begin with some definitions.

# A namespace is a mapping from names to objects. Most namespaces are currently 
# implemented as Python dictionaries, but that’s normally not noticeable in any 
# way (except for performance), and it may change in the future. Examples of 
# namespaces are: the set of built-in names (containing functions such as abs(), 
# and built-in exception names); the global names in a module; and the local names 
# in a function invocation. In a sense the set of attributes of an object also 
# form a namespace. The important thing to know about namespaces is that there is 
# absolutely no relation between names in different namespaces; for instance, two 
# different modules may both define a function maximize without confusion — users 
# of the modules must prefix it with the module name.

# By the way, I use the word attribute for any name following a dot — for example, 
# in the expression z.real, real is an attribute of the object z. Strictly speaking, 
# references to names in modules are attribute references: in the expression modname.
# funcname, modname is a module object and funcname is an attribute of it. In this 
# case there happens to be a straightforward mapping between the module’s attributes 
# and the global names defined in the module: they share the same namespace! (Except 
# for one thing. Module objects have a secret read-only attribute called __dict__ 
# which returns the dictionary used to implement the module’s namespace; the 
# name __dict__ is an attribute but not a global name. Obviously, using this 
# violates the abstraction of namespace implementation, and should be restricted 
# to things like post-mortem debuggers).

# Attributes may be read-only or writable. In the latter case, assignment to 
# attributes is possible. Module attributes are writable: you can write 
modname.the_answer = 42
# Writable attributes may also be deleted with the del statement. For example, 
del modname.the_answer 
# will remove the attribute the_answer from the object named by modname.

# Namespaces are created at different moments and have different lifetimes. 
# The namespace containing the built-in names is created when the Python 
# interpreter starts up, and is never deleted. The global namespace for a 
# module is created when the module definition is read in; normally, module 
# namespaces also last until the interpreter quits. The statements executed by 
# the top-level invocation of the interpreter, either read from a script file 
# or interactively, are considered part of a module called __main__, so they 
# have their own global namespace. (The built-in names actually also live in 
# a module; this is called builtins.)

# The local namespace for a function is created when the function is called, and 
# deleted when the function returns or raises an exception that is not handled 
# within the function. (Actually, forgetting would be a better way to describe 
# what actually happens.) Of course, recursive invocations each have their own 
# local namespace.

# A scope is a textual region of a Python program where a namespace is directly 
# accessible. “Directly accessible” here means that an unqualified reference to 
# a name attempts to find the name in the namespace.

# Although scopes are determined statically, they are used dynamically. At any 
# time during execution, there are 3 or 4 nested scopes whose namespaces are 
# directly accessible:

  # - the innermost scope, which is searched first, contains the local names

  # - the scopes of any enclosing functions, which are searched starting with 
  #   the nearest enclosing scope, contain non-local, but also non-global names

  # - the next-to-last scope contains the current module’s global names

  # - the outermost scope (searched last) is the namespace containing built-in names

# If a name is declared global, then all references and assignments go directly 
# to the next-to-last scope containing the module’s global names. To rebind 
# variables found outside of the innermost scope, the nonlocal statement can be 
# used; if not declared nonlocal, those variables are read-only (an attempt to 
# write to such a variable will simply create a new local variable in the 
# innermost scope, leaving the identically named outer variable unchanged).

# Usually, the local scope references the local names of the (textually) current 
# function. Outside functions, the local scope references the same namespace as the 
# global scope: the module’s namespace. Class definitions place yet another 
# namespace in the local scope.

# It is important to realize that scopes are determined textually: the global scope 
# of a function defined in a module is that module’s namespace, no matter from where 
# or by what alias the function is called. On the other hand, the actual search for 
# names is done dynamically, at run time.

# A special quirk of Python is that – if no global or nonlocal statement is in 
# effect – assignments to names always go into the innermost scope. Assignments 
# do not copy data — they just bind names to objects. The same is true for 
# deletions: the statement del x removes the binding of x from the namespace 
# referenced by the local scope. In fact, all operations that introduce new names 
# use the local scope: in particular, import statements and function definitions 
# bind the module or function name in the local scope.

# The global statement can be used to indicate that particular variables live in 
# the global scope and should be rebound there; the nonlocal statement indicates 
# that particular variables live in an enclosing scope and should be rebound there.


##### 9.2.1. Scopes and Namespaces Example #####

# This is an example demonstrating how to reference the different scopes and 
# namespaces, and how global and nonlocal affect variable binding:

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)  # it return spam = non local spam

scope_test()
print("In global scope:", spam)  # outside the function it returns spam = global spam

# Note how the local assignment (which is default) didn’t change scope_test's binding 
# of spam. The nonlocal assignment changed scope_test's binding of spam, and the 
# global assignment changed the module-level binding.

# You can also see that there was no previous binding for spam before the global 
# assignment.


##### 9.3. A First Look at Classes #####

# Classes introduce a little bit of new syntax, three new object types, and some 
# new semantics.


##### 9.3.1. Class Definition Syntax #####

# The simplest form of class definition looks like this:

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

# Class definitions, like function definitions (def statements) must be executed 
# before they have any effect. (You could conceivably place a class definition in 
# a branch of an if statement, or inside a function.)

# In practice, the statements inside a class definition will usually be function 
# definitions, but other statements are allowed, and sometimes useful — we’ll 
# come back to this later. The function definitions inside a class normally have 
# a peculiar form of argument list, dictated by the calling conventions for 
# methods — again, this is explained later.

# When a class definition is entered, a new namespace is created, and used as the 
# local scope — thus, all assignments to local variables go into this new namespace. 
# In particular, function definitions bind the name of the new function here.

# When a class definition is left normally (via the end), a class object is created. 
# This is basically a wrapper around the contents of the namespace created by the 
# class definition; we’ll learn more about class objects in the next section. 
# The original local scope (the one in effect just before the class definition 
# was entered) is reinstated, and the class object is bound here to the 
# class name given in the class definition header (ClassName in the example).


##### 9.3.2. Class Objects #####

# Class objects support two kinds of operations: attribute references and 
# instantiation.

# Attribute references use the standard syntax used for all attribute references 
# in Python: obj.name. Valid attribute names are all the names that were in the 
# class’s namespace when the class object was created. So, if the class definition 
# looked like this:

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

MyClass.i
MyClass.f
MyClass.f(0)  # returns 'hello world', 0 is just an argument but it is not used
MyClass.__doc__  # it returns the string in the functione """ A simple ... """

# Class instantiation uses function notation. Just pretend that the class object 
# is a parameterless function that returns a new instance of the class. 
# For example (assuming the above class):

x = MyClass()

# creates a new instance of the class and assigns this object to the local 
# variable x.

x.i
x.f() # returns 'hello world'

# The instantiation operation (“calling” a class object) creates an empty object. 
# Many classes like to create objects with instances customized to a specific initial 
# state. Therefore a class may define a special method named __init__(), like this:

def __init__(self):
    self.data = []

# When a class defines an __init__() method, class instantiation automatically 
# invokes __init__() for the newly created class instance. So in this example, 
# a new, initialized instance can be obtained by:

x = MyClass()

# Of course, the __init__() method may have arguments for greater flexibility. 
# In that case, arguments given to the class instantiation operator are passed on to 
# __init__(). For example,

# class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i


##### 9.3.3. Instance Objects #####

# Now what can we do with instance objects? The only operations understood by 
# instance objects are attribute references. There are two kinds of valid attribute 
# names: data attributes and methods.

# data attributes correspond to “instance variables” in Smalltalk, and to 
# “data members” in C++. Data attributes need not be declared; like local variables, 
# they spring into existence when they are first assigned to. For example, if x is 
# the instance of MyClass created above, the following piece of code will print the 
# value 16, without leaving a trace:

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
    print(x.counter)
del x.counter

# The other kind of instance attribute reference is a method. A method is a 
# function that “belongs to” an object. (In Python, the term method is not unique 
# to class instances: other object types can have methods as well. For example, 
# list objects have methods called append, insert, remove, sort, and so on. 
# However, in the following discussion, we’ll use the term method exclusively 
# to mean methods of class instance objects, unless explicitly stated otherwise.)

# Valid method names of an instance object depend on its class. By definition, 
# all attributes of a class that are function objects define corresponding methods 
# of its instances. So in our example, x.f is a valid method reference, since 
# MyClass.f is a function, but x.i is not, since MyClass.i is not. But x.f is 
# not the same thing as MyClass.f — it is a method object, not a function object.


##### 9.3.4. Method Objects #####

# Usually, a method is called right after it is bound:

x.f()

# In the MyClass example, this will return the string 'hello world'. 
# However, it is not necessary to call a method right away: x.f is a method 
# object, and can be stored away and called at a later time. For example:

x = MyClass()

xf = x.f
while True:
    print(xf())
# will continue to print hello world until the end of time.

# What exactly happens when a method is called? You may have noticed that x.f() was 
# called without an argument above, even though the function definition for f() 
# specified an argument. What happened to the argument? Surely Python raises an 
# exception when a function that requires an argument is called without any — even 
# if the argument isn’t actually used…

# Actually, you may have guessed the answer: the special thing about methods is 
# that the instance object is passed as the first argument of the function. In 
# our example, the call x.f() is exactly equivalent to MyClass.f(x). In general, 
# calling a method with a list of n arguments is equivalent to calling the 
# corresponding function with an argument list that is created by inserting the 
# method’s instance object before the first argument.

# If you still don’t understand how methods work, a look at the implementation 
# can perhaps clarify matters. When a non-data attribute of an instance is 
# referenced, the instance’s class is searched. If the name denotes a valid 
# class attribute that is a function object, a method object is created by 
# packing (pointers to) the instance object and the function object just 
# found together in an abstract object: this is the method object. When the 
# method object is called with an argument list, a new argument list is 
# constructed from the instance object and the argument list, and the function 
# object is called with this new argument list.


##### 9.3.5. Class and Instance Variables #####

# Generally speaking, instance variables are for data unique to each instance and 
# class variables are for attributes and methods shared by all instances of the 
# class:

class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs

e.kind                  # shared by all dogs

d.name                  # unique to d

>>> e.name                  # unique to e
'Buddy'

# As discussed in A Word About Names and Objects, shared data can have possibly 
# surprising effects with involving mutable objects such as lists and dictionaries. 
# For example, the tricks list in the following code should not be used as a 
# class variable because just a single list would be shared by all Dog instances:

class Dog:
    tricks = []             # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # unexpectedly shared by all dogs

# Correct design of the class should use an instance variable instead:

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
e.tricks


##### 9.4. Random Remarks #####

# If the same attribute name occurs in both an instance and in a class, then 
# attribute lookup prioritizes the instance:

class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)  # w2.purpose will be like w1.purpose

# Data attributes may be referenced by methods as well as by ordinary users 
# (“clients”) of an object. In other words, classes are not usable to implement 
# pure abstract data types. In fact, nothing in Python makes it possible to 
# enforce data hiding — it is all based upon convention. (On the other hand, 
# the Python implementation, written in C, can completely hide implementation 
# details and control access to an object if necessary; this can be used by 
# extensions to Python written in C.)

# Clients should use data attributes with care — clients may mess up invariants 
# maintained by the methods by stamping on their data attributes. Note that 
# clients may add data attributes of their own to an instance object without 
# affecting the validity of the methods, as long as name conflicts are 
# avoided — again, a naming convention can save a lot of headaches here.

# There is no shorthand for referencing data attributes (or other methods!) 
# from within methods. I find that this actually increases the readability of 
# methods: there is no chance of confusing local variables and instance variables 
# when glancing through a method.

# Often, the first argument of a method is called self. This is nothing more 
# than a convention: the name self has absolutely no special meaning to Python. 
# Note, however, that by not following the convention your code may be less 
# readable to other Python programmers, and it is also conceivable that a class 
# browser program might be written that relies upon such a convention.

# Any function object that is a class attribute defines a method for instances 
# of that class. It is not necessary that the function definition is textually 
# enclosed in the class definition: assigning a function object to a local 
# variable in the class is also ok. For example:

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g

f1(0, 8, 5)  # returns 8 whic is < 8 + 5
C.f(0, 3, 9) # returns 3 whic is < 3 + 9
C.g(0)   # returns 'hello world'
C.h(0)   # same as above

# Now f, g and h are all attributes of class C that refer to function objects, 
# and consequently they are all methods of instances of C — h being exactly 
# equivalent to g. Note that this practice usually only serves to confuse the 
# reader of a program.

# Methods may call other methods by using method attributes of the self argument:

class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
        # print(self.data)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
        # print(self.data)

temp = Bag()
temp.add('keys')

temp.addtwice('tissues')

temp.data  # is the list we created. temp.data is like self.data in the Class

print(temp.data)    

# Methods may reference global names in the same way as ordinary functions. The 
# global scope associated with a method is the module containing its definition. 
# (A class is never used as a global scope.) While one rarely encounters a good 
# reason for using global data in a method, there are many legitimate uses of 
# the global scope: for one thing, functions and modules imported into the global 
# scope can be used by methods, as well as functions and classes defined in it. 
# Usually, the class containing the method is itself defined in this global scope, 
# and in the next section we’ll find some good reasons why a method would want to 
# reference its own class.

# Each value is an object, and therefore has a class (also called its type). 
# It is stored as object.__class__.


##### 9.5. Inheritance #####







