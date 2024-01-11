
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on 01/11/2024 -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


# This tutorial introduces the reader informally to the basic concepts and features of 
# the Python language and system. It helps to have a Python interpreter handy for 
# hands-on experience, but all examples are self-contained, so the tutorial can be 
# read off-line as well.

# By the way, the language is named after the BBC show “Monty Python’s Flying Circus” 
# and has nothing to do with reptiles. Making references to Monty Python skits in 
# documentation is not only allowed, it is encouraged!


##### 2. Using the Python Interpreter #####


##### 2.1. Invoking the Interpreter #####

# The Python interpreter is usually installed as /usr/local/bin/python3.12 on those 
# machines where it is available; putting /usr/local/bin in your Unix shell’s 
# search path makes it possible to start it by typing the command:

python3.12

# On Windows machines where you have installed Python from the Microsoft Store, 
# the 

python3.12 

# command will be available. If you have the py.exe launcher installed, 
# you can use the 

py 

# command. See Excursus: Setting environment variables for other ways to 
# launch Python.

# Typing an end-of-file character (Control-D on Unix, Control-Z on Windows) at the 
# primary prompt causes the interpreter to exit with a zero exit status. If that 
# doesn’t work, you can exit the interpreter by typing the following command: 

quit()


##### 2.1.2. Interactive Mode #####

# When commands are read from a tty, the interpreter is said to be in interactive 
# mode. In this mode it prompts for the next command with the primary prompt, 
# usually three greater-than signs (>>>); for continuation lines it prompts with 
# the secondary prompt, by default three dots (...). The interpreter prints a 
# welcome message stating its version number and a copyright notice before printing 
# the first prompt:


##### 2.2. The Interpreter and Its Environment #####


##### 2.2.1. Source Code Encoding #####

# To declare an encoding other than the default one, a special comment line 
# should be added as the first line of the file. The syntax is as follows:

# -*- coding: encoding -*-

# where encoding is one of the valid codecs supported by Python.

# For example, to declare that Windows-1252 encoding is to be used, the first 
# line of your source code file should be:

# -*- coding: cp1252 -*-

# One exception to the first line rule is when the source code starts with a 
# UNIX “shebang” line. In this case, the encoding declaration should be added as 
# the second line of the file. For example:

#!/usr/bin/env python3
# -*- coding: cp1252 -*-


