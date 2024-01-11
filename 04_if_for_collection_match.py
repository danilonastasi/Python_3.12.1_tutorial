
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on __________  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


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

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# Note the last block: the “variable name” _ acts as a wildcard and never fails 
# to match. If no case matches, none of the branches is executed.

# You can combine several literals in a single pattern using | (“or”):

def http_error(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"

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


