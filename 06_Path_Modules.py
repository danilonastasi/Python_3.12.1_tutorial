
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on __________  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


##### 6. Modules #####

# If you quit from the Python interpreter and enter it again, the definitions you have 
# made (functions and variables) are lost. Therefore, if you want to write a somewhat 
# longer program, you are better off using a text editor to prepare the input for the 
# interpreter and running it with that file as input instead. This is known as creating 
# a script. As your program gets longer, you may want to split it into several files 
# for easier maintenance. You may also want to use a handy function that you’ve 
# written in several programs without copying its definition into each program.

# To support this, Python has a way to put definitions in a file and use them in a 
# script or in an interactive instance of the interpreter. Such a file is called 
# a module; definitions from a module can be imported into other modules or into 
# the main module (the collection of variables that you have access to in a script 
# executed at the top level and in calculator mode).

# A module is a file containing Python definitions and statements. The file name 
# is the module name with the suffix .py appended. Within a module, the 
# module’s name (as a string) is available as the value of the global 
# variable __name__. For instance, use your favorite text editor to create a 
# file called fibo.py in the current directory with the following contents:

##### to be continued #####


##### from the website https://www.dummies.com/article/technology/programming-web-design/python/how-to-find-path-information-in-python-148336/
##### Path information sources #####

# Environment variables: Python environment variables, such as PYTHONPATH, tell 
#                        Python where to find modules on disk.

# Current directory: You can change the current Python directory so that it can 
#                    locate any modules used by your application.

# Default directories: Even when you don’t define any environment variables and the 
# current directory doesn’t yield any usable modules, Python can still find its own 
# libraries in the set of default directories that are included as part of its own 
# path information.

##### How to find path information #####

# It’s helpful to know the current path information because the lack of a path 
# can cause your application to fail. The following steps demonstrate how you 
# can obtain path information:

import sys
for p in sys.path: print(p)

##### Another way to find paths #####

# The sys.path attribute is reliable but may not always contain every path that 
# Python can see. If you don’t see a needed path, you can always check in another 
# place that Python looks for information. The following steps show how to perform 
# this task:

import os
os.environ['PYTHONPATH'].split(os.pathsep)

# When you have a PYTHONPATH environment variable defined, you see a list of paths, 
# as shown in the figure below. However, if you don’t have the environment variable 
# defined, you see an error message instead.

# You can also add and remove items from sys.path. For example, if you want to add 
# the current working directory to the list of packages, you type 

sys.path.append(os.getcwd()) 

# and press Enter

# When you list the sys.path contents again, you see that the new entry is added to 
# the end of the list. Likewise, when you want to remove an entry you type 

sys.path.remove(os.getcwd()) 

# and press Enter. The addition is present only during the current session.


##### 6. Modules - continue #####

# For instance, use your favorite text editor to create a file called fibo.py 
# in the current directory with the following contents:
# I use Notepad

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Now enter the Python interpreter and import this module with the following command:

import fibo

# This does not add the names of the functions defined in fibo directly to the 
# current namespace (see Python Scopes and Namespaces for more details); it 
# only adds the module name fibo there. Using the module name you can access the 
# functions:

fibo.fib(1000)   # fibo is the module, fib is the function (def)

fibo.fib2(100)

fibo.__name__  # we get fibo

# If you intend to use a function often you can assign it to a local name:

fib = fibo.fib
fib(500)


##### 6.1. More on Modules #####

# A module can contain executable statements as well as function definitions. 
# These statements are intended to initialize the module. They are executed only 
# the first time the module name is encountered in an import statement
# (in fact function definitions are also ‘statements’ that are ‘executed’; the 
# execution of a module-level function definition adds the function name to 
# the module’s global namespace). (They are also run if the file is executed as 
# a script.)

# Each module has its own private namespace, which is used as the global namespace 
# by all functions defined in the module. Thus, the author of a module can use 
# global variables in the module without worrying about accidental clashes with a 
# user’s global variables. On the other hand, if you know what you are doing you 
# can touch a module’s global variables with the same notation used to refer to its 
# functions, modname.itemname.

# Modules can import other modules. It is customary but not required to place all 
# import statements at the beginning of a module (or script, for that matter). 
# The imported module names, if placed at the top level of a module (outside any 
# functions or classes), are added to the module’s global namespace.

# There is a variant of the import statement that imports names from a module 
# directly into the importing module’s namespace. For example:

from fibo import fib, fib2
fib(500)

# This does not introduce the module name from which the imports are taken in the 
# local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

from fibo import *
fib(500)

# This imports all names except those beginning with an underscore (_). In most 
# cases Python programmers do not use this facility since it introduces an unknown 
# set of names into the interpreter, possibly hiding some things you have already 
# defined.

# Note that in general the practice of importing * from a module or package is 
# frowned upon, since it often causes poorly readable code. However, it is okay 
# to use it to save typing in interactive sessions.

# If the module name is followed by as, then the name following as is bound 
# directly to the imported module.

import fibo as fib
fib.fib(500)

# This is effectively importing the module in the same way that import fibo 
# will do, with the only difference of it being available as fib.

# It can also be used when utilising from with similar effects:

from fibo import fib as fibonacci
fibonacci(500)

## Note For efficiency reasons, each module is only imported once per interpreter 
# session. Therefore, if you change your modules, you must restart the 
# interpreter – or, if it’s just one module you want to test interactively, 
# use importlib.reload(), e.g. import importlib; importlib.reload(modulename).


##### 6.1.1. Executing modules as scripts #####








