
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on 01/16/2024  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


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

# When you run a Python module with

# python fibo.py <arguments> from the prompt and not from Python

# the code in the module will be executed, just as if you imported it, but 
# with the __name__ set to "__main__". That means that by adding this code 
# at the end of your module, the module you created fibo.py

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    
# you can make the file usable as a script as well as an importable module, 
# because the code that parses the command line only runs if the module is 
# executed as the “main” file:

# from the prompt, I think in the path where you saved the fibo.py module
python fibo.py 50
# 0 1 1 2 3 5 8 13 21 34

# If the module is imported, the code is not run, from Python:

import fibo   # not clear what happens

# This is often used either to provide a convenient user interface to a module, or 
# for testing purposes (running the module as a script executes a test suite).


##### 6.2. Standard Modules #####

# Python comes with a library of standard modules, described in a separate document, 
# the Python Library Reference (“Library Reference” hereafter). Some modules are 
# built into the interpreter; these provide access to operations that are not part 
# of the core of the language but are nevertheless built in, either for efficiency 
# or to provide access to operating system primitives such as system calls. The 
# set of such modules is a configuration option which also depends on the 
# underlying platform. For example, the winreg module is only provided on Windows 
# systems. One particular module deserves some attention: sys, which is built 
# into every Python interpreter. The variables sys.ps1 and sys.ps2 define the 
# strings used as primary and secondary prompts:

import sys
sys.ps1

sys.ps2

sys.ps1 = 'C> '

# These two variables are only defined if the interpreter is in interactive mode.

# The variable 

sys.path 

# is a list of strings that determines the interpreter’s 
# search path for modules. It is initialized to a default path taken from the 
# environment variable PYTHONPATH, or from a built-in default if PYTHONPATH is 
# not set. You can modify it using standard list operations:

import sys
sys.path.append('/ufs/guido/lib/python')


##### 6.3. The dir() Function #####

# The built-in function dir() is used to find out which names a module defines. 
# It returns a sorted list of strings:

import fibo, sys
dir(fibo)

dir(sys)  

# Without arguments, dir() lists the names you have defined currently:

a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()

# Note that it lists all types of names: variables, modules, functions, etc.

# dir() does not list the names of built-in functions and variables. If you want 
# a list of those, they are defined in the standard module builtins:

import builtins
dir(builtins)  


##### 6.4. Packages #####

# Packages are a way of structuring Python’s module namespace by using “dotted 
# module names”. For example, the module name A.B designates a submodule named B 
# in a package named A. Just like the use of modules saves the authors of different 
# modules from having to worry about each other’s global variable names, the use 
# of dotted module names saves the authors of multi-module packages like NumPy 
# or Pillow from having to worry about each other’s module names.

# Suppose you want to design a collection of modules (a “package”) for the uniform 
# handling of sound files and sound data. There are many different sound file 
# formats (usually recognized by their extension, for example: .wav, .aiff, .au), 
# so you may need to create and maintain a growing collection of modules for the 
# conversion between the various file formats. There are also many different 
# operations you might want to perform on sound data (such as mixing, adding echo, 
# applying an equalizer function, creating an artificial stereo effect), so in 
# addition you will be writing a never-ending stream of modules to perform these 
# operations. Here’s a possible structure for your package (expressed in terms 
# of a hierarchical filesystem):

# of course this code will not work, this is the ipothetical package

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

# When importing the package, Python searches through the directories on sys.path 
# looking for the package subdirectory.

# The __init__.py files are required to make Python treat directories containing 
# the file as packages (unless using a namespace package, a relatively advanced 
# feature). This prevents directories with a common name, such as string, from 
# unintentionally hiding valid modules that occur later on the module search path. 
# In the simplest case, __init__.py can just be an empty file, but it can also 
# execute initialization code for the package or set the __all__ variable, 
# described later.

# Users of the package can import individual modules from the package, for example:

import sound.effects.echo  # error because the model doesn't exist

# This loads the submodule sound.effects.echo. It must be referenced with 
# its full name.

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)  # error, is missing

# An alternative way of importing the submodule is:

from sound.effects import echo # error, is missing

# This also loads the submodule echo, and makes it available without its package 
# prefix, so it can be used as follows:

echo.echofilter(input, output, delay=0.7, atten=4) # error, is missing

# Yet another variation is to import the desired function or variable directly:

from sound.effects.echo import echofilter  # error, is missing

# Again, this loads the submodule echo, but this makes its function echofilter() 
# directly available:

echofilter(input, output, delay=0.7, atten=4) # error, is missing

# Note that when using from package import item, the item can be either a 
# submodule (or subpackage) of the package, or some other name defined in the 
# package, like a function, class or variable. The import statement first tests 
# whether the item is defined in the package; if not, it assumes it is a module 
# and attempts to load it. If it fails to find it, an ImportError exception 
# is raised.

# Contrarily, when using syntax like import item.subitem.subsubitem, each item 
# except for the last must be a package; the last item can be a module or a 
# package but can’t be a class or function or variable defined in the 
# previous item.


##### 6.4.1. Importing * From a Package #####

# Now what happens when the user writes from sound.effects import *? Ideally, one 
# would hope that this somehow goes out to the filesystem, finds which submodules 
# are present in the package, and imports them all. This could take a long time 
# and importing sub-modules might have unwanted side-effects that should only 
# happen when the sub-module is explicitly imported.

# The only solution is for the package author to provide an explicit index of 
# the package. The import statement uses the following convention: if a 
# package’s __init__.py code defines a list named __all__, it is taken to be the 
# list of module names that should be imported when from package import * is 
# encountered. It is up to the package author to keep this list up-to-date 
# when a new version of the package is released. Package authors may also decide 
# not to support it, if they don’t see a use for importing * from their package. 
# For example, the file sound/effects/__init__.py could contain the following code:

# __all__ = ["echo", "surround", "reverse"]

# This would mean that from sound.effects import * would import the three named 
# submodules of the sound.effects package.

# Be aware that submodules might become shadowed by locally defined names. 
# For example, if you added a reverse function to the sound/effects/__init__.py file, 
# the from sound.effects import * would only import the two submodules echo and 
# surround, but not the reverse submodule, because it is shadowed by the locally 
# defined reverse function:

# __all__ = [
#     "echo",      # refers to the 'echo.py' file
#     "surround",  # refers to the 'surround.py' file
#     "reverse",   # !!! refers to the 'reverse' function now !!!
# ]

# def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
#     return msg[::-1]    #     in the case of a 'from sound.effects import *'

# It also includes any submodules of the package that were explicitly loaded by 
# previous import statements. Consider this code:

import sound.effects.echo  # error, is missing
import sound.effects.surround  # error, is missing
from sound.effects import *  # error, is missing

# In this example, the echo and surround modules are imported in the current 
# namespace because they are defined in the sound.effects package when the 
# from...import statement is executed. (This also works when __all__ is defined.)

# Although certain modules are designed to export only names that follow certain 
# patterns when you use import *, it is still considered bad practice in 
# production code.

# Remember, there is nothing wrong with using from package import specific_submodule! 
# In fact, this is the recommended notation unless the importing module needs 
# to use submodules with the same name from different packages.













