
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on _________ -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


##### 3. An Informal Introduction to Python #####

# Comments in Python start with the hash character, #, and extend to the end of the 
# physical line.

# Some examples:

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."


##### 3.1. Using Python as a Calculator #####


Let’s try some simple Python commands. Start the interpreter and wait for the primary prompt, >>>. (It shouldn’t take long.)

3.1.1. Numbers
The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / can be used to perform arithmetic; parentheses (()) can be used for grouping. For example:

>>>
2 + 2

50 - 5*6

(50 - 5*6) / 4

8 / 5  # division always returns a floating point number

The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.

Division (/) always returns a float. To do floor division and get an integer result you can use the // operator; to calculate the remainder you can use %:
