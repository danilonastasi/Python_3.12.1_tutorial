
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


# Let’s try some simple Python commands. Start the interpreter and wait for the primary prompt, >>>. (It shouldn’t take long.)


##### 3.1.1. Numbers #####

# The interpreter acts as a simple calculator: you can type an expression at it 
# and it will write the value. Expression syntax is straightforward: the 
# operators +, -, * and / can be used to perform arithmetic; parentheses (()) 
# can be used for grouping. For example:

2 + 2

50 - 5*6

(50 - 5*6) / 4

8 / 5  # division always returns a floating point number

# The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional 
# part (e.g. 5.0, 1.6) have type float. We will see more about numeric types 
# later in the tutorial.

# Division (/) always returns a float. To do floor division and get an integer 
# result you can use the // operator; to calculate the remainder you can use %:

17 / 3  # classic division returns a float

17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

5 * 3 + 2  # floored quotient * divisor + remainder

# With Python, it is possible to use the ** operator to calculate powers 1:

5 ** 2  # 5 squared

2 ** 7  # 2 to the power of 7

# The equal sign (=) is used to assign a value to a variable. Afterwards, 
# no result is displayed before the next interactive prompt:

width = 20
height = 5 * 9
width * height

# There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:

4 * 3.75 - 1

# In interactive mode, the last printed expression is assigned to the variable _. 
# This means that when you are using Python as a desk calculator, it is somewhat 
# easier to continue calculations, for example:

tax = 12.5 / 100
price = 100.50
price * tax

price + _

round(_, 2)  # remove 2 decimal places from the _ variable

# This variable should be treated as read-only by the user. Don’t explicitly assign 
# a value to it — you would create an independent local variable with the same name 
# masking the built-in variable with its magic behavior.

# In addition to int and float, Python supports other types of numbers, such as 
# Decimal and Fraction. Python also has built-in support for complex numbers, and 
# uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).







