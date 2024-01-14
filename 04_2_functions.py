
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on 01/14/2024  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


##### 4.7. Defining Functions #####

# We can create a function that writes the Fibonacci series to an arbitrary boundary:

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# The keyword def introduces a function definition. It must be followed by the 
# function name and the parenthesized list of formal parameters. The statements 
# that form the body of the function start at the next line, and must be indented.

# The first statement of the function body can optionally be a string literal; 
# this string literal is the function’s documentation string, or docstring. (More 
# about docstrings can be found in the section Documentation Strings.) There are 
# tools which use docstrings to automatically produce online or printed documentation, 
# or to let the user interactively browse through code; it’s good practice to 
# include docstrings in code that you write, so make a habit of it.

# A function definition associates the function name with the function object in 
# the current symbol table. The interpreter recognizes the object pointed to by 
# that name as a user-defined function. Other names can also point to that same 
# function object and can also be used to access the function:

fib

f = fib
f(100)

# Coming from other languages, you might object that fib is not a function but 
# a procedure since it doesn’t return a value. In fact, even functions without 
# a return statement do return a value, albeit a rather boring one. This value 
# is called None (it’s a built-in name). Writing the value None is normally 
# suppressed by the interpreter if it would be the only value written. You can 
# see it if you really want to using print():

fib(0)
print(fib(0))

# It is simple to write a function that returns a list of the numbers of the 
# Fibonacci series, instead of printing it:

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result

# This example, as usual, demonstrates some new Python features:

  # - The return statement returns with a value from a function. return without an 
  #   expression argument returns None. Falling off the end of a function also 
  #   returns None.

  # - The statement result.append(a) calls a method of the list object result. 
  #   A method is a function that ‘belongs’ to an object and is named obj.methodname, 
  #   where obj is some object (this may be an expression), and methodname is the 
  #   name of a method that is defined by the object’s type. Different types define 
  #   different methods. Methods of different types may have the same name without 
  #   causing ambiguity. (It is possible to define your own object types and methods, 
  #   using classes, see Classes) The method append() shown in the example is defined 
  #   for list objects; it adds a new element at the end of the list. In this example 
  #   it is equivalent to result = result + [a], but more efficient.


##### 4.8. More on Defining Functions #####

# It is also possible to define functions with a variable number of arguments. 
# There are three forms, which can be combined.


##### 4.8.1. Default Argument Values #####

# The most useful form is to specify a default value for one or more arguments. 
# This creates a function that can be called with fewer arguments than it is 
# defined to allow. For example:

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}: # it is satisfied for y, ye, yes 
            return True   # with return we stop the function
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False  # with return we stop the function
        retries = retries - 1   # it happens if we answer different from options above
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# This function can be called in several ways:

  # - giving only the mandatory argument: 
        ask_ok('Do you really want to quit?')

  # - giving one of the optional arguments: 
        ask_ok('OK to overwrite the file?', 2)

# or even giving all arguments: 
        ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# This example also introduces the in keyword. This tests whether or not a 
# sequence contains a certain value.

# The default values are evaluated at the point of function definition in the 
# defining scope, so that

i = 5

def f(arg=i):
    print(arg)

i = 6
f()  # will print 5

# Important warning: The default value is evaluated only once. This makes a 
# difference when the default is a mutable object such as a list, dictionary, 
# or instances of most classes. For example, the following function accumulates 
# the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# This will print

  # [1]
  # [1, 2]
  # [1, 2, 3]

# If you don’t want the default to be shared between subsequent calls, you can 
# write the function like this instead:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


##### 4.8.2. Keyword Arguments #####

# Functions can also be called using keyword arguments of the form kwarg=value. 
# For instance, the following function:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# accepts one required argument (voltage) and three optional arguments 
# (state, action, and type). This function can be called in any of the following 
# ways:

parrot(1000)                                                # 1 positional argument
parrot(voltage=1000)  # same results as above               # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')                   # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000) # same as above   # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')               # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')        # 1 positional, 1 keyword

# but all the following calls would be invalid:

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

# When a final formal parameter of the form **name is present, it receives a 
# dictionary (see Mapping Types — dict) containing all keyword arguments except 
# for those corresponding to a formal parameter. This may be combined with a formal 
# parameter of the form *name (described in the next subsection) which receives a 
# tuple containing the positional arguments beyond the formal parameter list. 
# (*name must occur before **name.) For example, if we define a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

  # It could be called like this:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Note that the order in which the keyword arguments are printed is guaranteed 
# to match the order in which they were provided in the function call.


##### 4.8.3. Special parameters #####

# By default, arguments may be passed to a Python function either by position or 
# explicitly by keyword. For readability and performance, it makes sense to 
# restrict the way arguments can be passed so that a developer need only look at 
# the function definition to determine if items are passed by position, by 
# position or keyword, or by keyword.

# A function definition may look like:

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only

# where / and * are optional. If used, these symbols indicate the kind of parameter 
# by how the arguments may be passed to the function: positional-only, 
# positional-or-keyword, and keyword-only. Keyword parameters are also referred to 
# as named parameters.


##### 4.8.3.4. Function Examples #####

# Consider the following example function definitions paying close attention to 
# the markers / and *:

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# The first function definition, standard_arg, the most familiar form, places 
# no restrictions on the calling convention and arguments may be passed by position 
# or keyword:

standard_arg(2)
standard_arg(arg=2)

# The second function pos_only_arg is restricted to only use positional parameters 
# as there is a / in the function definition:

pos_only_arg(1)
pos_only_arg(arg=1)  # error

# The third function kwd_only_args only allows keyword arguments as indicated by 
# a * in the function definition:

kwd_only_arg(3)  # error
kwd_only_arg(arg=3)

# And the last uses all three calling conventions in the same function definition:

combined_example(1, 2, 3)   # error
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3)  # error

# Finally, consider this function definition which has a potential collision 
# between the positional argument name and **kwds which has name as a key:

def foo(name, **kwds):
    return 'name' in kwds

# There is no possible call that will make it return True as the keyword 'name' 
# will always bind to the first parameter. For example:

foo(1, **{'name': 2}) # error

# But using / (positional only arguments), it is possible since it allows name as a 
# positional argument and 'name' as a key in the keyword arguments:

def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})

# In other words, the names of positional-only parameters can be used 
# in **kwds without ambiguity.


##### 4.8.4. Arbitrary Argument Lists #####

# Finally, the least frequently used option is to specify that a function can be 
# called with an arbitrary number of arguments. These arguments will be wrapped up 
# in a tuple (see Tuples and Sequences). Before the variable number of arguments, 
# zero or more normal arguments may occur.

# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))

# Normally, these variadic arguments will be last in the list of formal parameters, 
# because they scoop up all remaining input arguments that are passed to the 
# function. Any formal parameters which occur after the *args parameter are 
# ‘keyword-only’ arguments, meaning that they can only be used as keywords rather 
# than positional arguments.

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")


##### 4.8.5. Unpacking Argument Lists #####

# The reverse situation occurs when the arguments are already in a list or tuple 
# but need to be unpacked for a function call requiring separate positional arguments. 
# For instance, the built-in range() function expects separate start and stop 
# arguments. If they are not available separately, write the function call with 
# the *-operator to unpack the arguments out of a list or tuple:

list(range(3, 6))            # normal call with separate arguments

args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list

# In the same fashion, dictionaries can deliver keyword arguments with 
# the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


##### 4.8.6. Lambda Expressions #####

# Small anonymous functions can be created with the lambda keyword. This function 
# returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be 
# used wherever function objects are required. They are syntactically restricted 
# to a single expression. Semantically, they are just syntactic sugar for a normal 
# function definition. Like nested function definitions, lambda functions can 
# reference variables from the containing scope:

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)

# The above example uses a lambda expression to return a function. Another use is 
# to pass a small function as an argument:

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


##### 4.8.7. Documentation Strings #####

# Here are some conventions about the content and formatting of documentation strings.

# The first line should always be a short, concise summary of the object’s purpose. 
# For brevity, it should not explicitly state the object’s name or type, since 
# these are available by other means (except if the name happens to be a verb 
# describing a function’s operation). This line should begin with a capital letter 
# and end with a period.

# If there are more lines in the documentation string, the second line should be 
# blank, visually separating the summary from the rest of the description. The 
# following lines should be one or more paragraphs describing the object’s calling 
# conventions, its side effects, etc.

# Here is an example of a multi-line docstring:

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


##### 4.8.8. Function Annotations #####

# Function annotations are completely optional metadata information about the types 
# used by user-defined functions (see PEP 3107 and PEP 484 for more information).

# Annotations are stored in the __annotations__ attribute of the function as a 
# dictionary and have no effect on any other part of the function. Parameter 
# annotations are defined by a colon after the parameter name, followed by an 
# expression evaluating to the value of the annotation. Return annotations are 
# defined by a literal ->, followed by an expression, between the parameter list 
# and the colon denoting the end of the def statement. The following example has 
# a required argument, an optional argument, and the return value annotated:

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
f('cheese', 'apples')


##### 4.9. Intermezzo: Coding Style #####

# Now that you are about to write longer, more complex pieces of Python, it is a 
# good time to talk about coding style. Most languages can be written 
# (or more concise, formatted) in different styles; some are more readable 
# than others. Making it easy for others to read your code is always a good idea, 
# and adopting a nice coding style helps tremendously for that.

# For Python, PEP 8 has emerged as the style guide that most projects adhere to; 
# it promotes a very readable and eye-pleasing coding style. Every Python developer 
# should read it at some point; here are the most important points extracted for you:

    # - Use 4-space indentation, and no tabs.

    # - 4 spaces are a good compromise between small indentation (allows greater 
    #   nesting depth) and large indentation (easier to read). Tabs introduce 
    #   confusion, and are best left out.

    # - Wrap lines so that they don’t exceed 79 characters.

    # - This helps users with small displays and makes it possible to have 
    #   several code files side-by-side on larger displays.

    # - Use blank lines to separate functions and classes, and larger blocks of 
    #   code inside functions.

    # - When possible, put comments on a line of their own.

    # - Use docstrings.

    # - Use spaces around operators and after commas, but not directly inside 
    #   bracketing constructs: a = f(1, 2) + g(3, 4).

    # - Name your classes and functions consistently; the convention is to use 
    #   UpperCamelCase for classes and lowercase_with_underscores for functions 
    #   and methods. Always use self as the name for the first method argument 
    #   (see A First Look at Classes for more on classes and methods).

    # - Don’t use fancy encodings if your code is meant to be used in international 
    #   environments. Python’s default, UTF-8, or even plain ASCII work best in 
    #   any case.

    # - Likewise, don’t use non-ASCII characters in identifiers if there is only 
    #   the slightest chance people speaking a different language will read or 
    #   maintain the code.











