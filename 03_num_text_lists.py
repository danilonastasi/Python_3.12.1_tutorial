
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on 01/11/2024  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


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


##### 3.1.2. Text #####

# Python can manipulate text (represented by type str, so-called “strings”) 
# as well as numbers. This includes characters “!”, words “rabbit”, names “Paris”, 
# sentences “Got your back.”, etc. “Yay! :)”. They can be enclosed in single 
# quotes ('...') or double quotes ("...") with the same result.

'spam eggs'  # single quotes

"Paris rabbit got your back :)! Yay!"  # double quotes

'1975'  # digits and numerals enclosed in quotes are also strings

# To quote a quote, we need to “escape” it, by preceding it with \. Alternatively, 
# we can use the other type of quotation marks:

'doesn\'t'  # use \' to escape the single quote...

"doesn't"  # ...or use double quotes instead

'"Yes," they said.'

"\"Yes,\" they said."

'"Isn\'t," they said.'  # it doesn/t work, let's try in this way:
temp = '"Isn\'t," they said.'
print(temp) # now it works

# In the Python shell, the string definition and output string can look different. 
# The print() function produces a more readable output, by omitting the enclosing 
# quotes and by printing escaped and special characters:

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string

print(s)  # with print(), special characters are interpreted, so \n produces 
          # new line

# If you don’t want characters prefaced by \ to be interpreted as special 
# characters, you can use raw strings by adding an r before the first quote:

print('C:\some\name')  # here \n means newline! we get a warning

print(r'C:\some\name')  # note the r before the quote

# There is one subtle aspect to raw strings: a raw string may not end in an 
# odd number of \ characters; see the FAQ entry for more information and 
# workarounds.

# String literals can span multiple lines. One way is using triple-quotes: 
# """...""" or '''...'''. End of lines are automatically included in the string, 
# but it’s possible to prevent this by adding a \ at the end of the line. 
# The following example:

print("""\  # in this way, with \ we skip the firs empty line
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# (note that the initial newline is not included)

# Strings can be concatenated (glued together) with the + operator, and repeated with *:

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

# Two or more string literals (i.e. the ones enclosed between quotes) next to 
# each other are automatically concatenated.

'Py' 'thon'

# This feature is particularly useful when you want to break long strings:

text = ('Put several strings within parentheses '
        'to have them joined together.') # it runs a line with long string
text

# This only works with two literals though, not with variables or expressions:

prefix = 'Py'
prefix 'thon'  # error # can't concatenate a variable and a string literal

# If you want to concatenate variables or a variable and a literal, use +:

prefix + 'thon'

# Strings can be indexed (subscripted), with the first character having index 0. 
# There is no separate character type; a character is simply a string of size one:

word = 'Python'
word[0]  # character in position 0

word[5]  # character in position 5

# Indices may also be negative numbers, to start counting from the right:

word[-1]  # last character

word[-2]  # second-last character

word[-6]

# In addition to indexing, slicing is also supported. While indexing is used 
# to obtain individual characters, slicing allows you to obtain a substring:

word[0:2]  # characters from position 0 (included) to 2 (excluded)

word[2:5]  # characters from position 2 (included) to 5 (excluded)

# Slice indices have useful defaults; an omitted first index defaults to zero, 
# an omitted second index defaults to the size of the string being sliced.

word[:2]   # character from the beginning to position 2 (excluded)

word[4:]   # characters from position 4 (included) to the end

word[-2:]  # characters from the second-last (included) to the end, right direction

# Note how the start is always included, and the end always excluded. This makes 
# sure that s[:i] + s[i:] is always equal to s:

word[:2] + word[2:]

word[:4] + word[4:]

# For non-negative indices, the length of a slice is the difference of the indices, 
# if both are within bounds. For example, the length of word[1:3] is 2.

# Attempting to use an index that is too large will result in an error:

word[42]  # error # the word only has 6 characters

# However, out of range slice indexes are handled gracefully when used for slicing:

word[4:42]  # it works also if the word is shorter than 42 characters

word[42:]  # no error but it will be empty

# Python strings cannot be changed — they are immutable. Therefore, assigning to 
# an indexed position in the string results in an error:

word[0] = 'J' # error

word[2:] = 'py' # error

# If you need a different string, you should create a new one:

'J' + word[1:]  # we add J to index 0 and we sum index 1: to J

word[:2] + 'py'  # we get the letters in index 0,1 and we sum py

# The built-in function len() returns the length of a string:

s = 'supercalifragilisticexpialidocious'
len(s)

# See also:

  # Text Sequence Type — str
    # Strings are examples of sequence types, and support the common operations 
    # supported by such types.

  # String Methods
    # Strings support a large number of methods for basic transformations 
    # and searching.

  # f-strings
    # String literals that have embedded expressions.

  # Format String Syntax
    # Information about string formatting with str.format().

  # printf-style String Formatting
    # The old formatting operations invoked when strings are the left operand 
    # of the % operator are described in more detail here.


##### 3.1.3. Lists #####

# Python knows a number of compound data types, used to group together other values. 
# The most versatile is the list, which can be written as a list of comma-separated 
# values (items) between square brackets. Lists might contain items of different 
# types, but usually the items all have the same type.

squares = [1, 4, 9, 16, 25]
squares

# Like strings (and all other built-in sequence types), lists can be 
# indexed and sliced:

squares[0]  # indexing returns the item

squares[-1]

squares[-3:]  # slicing returns a new list

# All slice operations return a new list containing the requested elements. 
# This means that the following slice returns a shallow copy of the list:

squares[:]

# Lists also support operations like concatenation:

squares + [36, 49, 64, 81, 100]

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is 
# possible to change their content:

cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!

cubes[3] = 64  # replace the wrong value
cubes

# You can also add new items at the end of the list, by using the 
# list.append() 
# method (we will see more about methods later):

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes

# Assignment to slices is also possible, and this can even change the size of 
# the list or clear it entirely:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# replace some values
letters[2:5] = ['C', 'D', 'E']
letters

# now remove them
letters[2:5] = []
letters

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

# The built-in function len() also applies to lists:

letters = ['a', 'b', 'c', 'd']
len(letters)

# It is possible to nest lists (create lists containing other lists), for example:

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]  # we create a new list which contains two list, one in index 0  
            # and one in index 1, so the lenght will be 2
x

x[0]  # we get the first list

x[0][1]  # we get the second value, index 1, of the first list


##### 3.2. First Steps Towards Programming #####

# Of course, we can use Python for more complicated tasks than adding two and two 
# together. For instance, we can write an initial sub-sequence of the 
# Fibonacci series as follows:

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1 # multiple assignment: the variables a and b simultaneously get 
            # the new values 0 and 1.
while a < 10:  # executes as long as the condition (here: a < 10) remains true
    print(a)  # writes the value of the argument(s) it is given.
    a, b = b, a+b 

# The keyword argument end can be used to avoid the newline after the output, 
# or end the output with a different string:

a, b = 0, 1
while a < 1000:
    print(a, end=',') # argument end to avoid the newline after the output
    a, b = b, a+b

# In Python, like in C, any non-zero integer value is true; zero is false. 
# The condition may also be a string or list value, in fact any sequence; 
# anything with a non-zero length is true, empty sequences are false. The test 
# used in the example is a simple comparison. The standard comparison operators 
# are written the same as in C: < (less than), > (greater than), == (equal to), 
# <= (less than or equal to), >= (greater than or equal to) and != (not equal to).

# The body of the loop is indented: indentation is Python’s way of grouping 
# statements. At the interactive prompt, you have to type a tab or space(s) for 
# each indented line.
# Note that each line within a basic block must be indented by the same amount.

# Strings are printed without quotes, and a space is inserted between items, 
# so you can format things nicely, like this:

i = 256*256
print('The value of i is', i)


