
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on _________  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


##### 5.3. Tuples and Sequences #####

# We saw that lists and strings have many common properties, such as indexing and 
# slicing operations. They are two examples of sequence data types 
# (see Sequence Types — list, tuple, range). Since Python is an evolving language, 
# other sequence data types may be added. There is also another standard sequence 
# data type: the tuple.

# A tuple consists of a number of values separated by commas, for instance:

t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

# As you see, on output tuples are always enclosed in parentheses, so that nested 
# tuples are interpreted correctly; they may be input with or without surrounding 
# parentheses, although often parentheses are necessary anyway (if the tuple is 
# part of a larger expression). It is not possible to assign to the individual items 
# of a tuple, however it is possible to create tuples which contain mutable objects, 
# such as lists.

# Though tuples may seem similar to lists, they are often used in different 
# situations and for different purposes. Tuples are immutable, and usually contain 
# a heterogeneous sequence of elements that are accessed via unpacking (see later 
# in this section) or indexing (or even by attribute in the case of namedtuples). 
# Lists are mutable, and their elements are usually homogeneous and are accessed by 
# iterating over the list.

# A special problem is the construction of tuples containing 0 or 1 items: 
# the syntax has some extra quirks to accommodate these. Empty tuples are 
# constructed by an empty pair of parentheses; a tuple with one item is constructed 
# by following a value with a comma (it is not sufficient to enclose a single value 
# in parentheses). Ugly, but effective. For example:

empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)

len(singleton)

singleton

# The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the 
# values 12345, 54321 and 'hello!' are packed together in a tuple. The reverse 
# operation is also possible:

x, y, z = t  # we get for every variable s value in t tuple

# This is called, appropriately enough, sequence unpacking and works for any 
# sequence on the right-hand side. Sequence unpacking requires that 
# there are as many variables on the left side of the equals sign as there are 
# elements in the sequence. Note that multiple assignment is really just a 
# combination of tuple packing and sequence unpacking.


##### 5.4. Sets #####

# Python also includes a data type for sets. A set is an unordered collection with 
# no duplicate elements. Basic uses include membership testing and eliminating 
# duplicate entries. Set objects also support mathematical operations like union, 
# intersection, difference, and symmetric difference.

# Curly braces or the set() function can be used to create sets. Note: to create 
# an empty set you have to use set(), not {}; the latter creates an empty dictionary, 
# a data structure that we discuss in the next section.

# Here is a brief demonstration:

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket    # True             # fast membership testing

'crabgrass' in basket  # False


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a

a - b    # it removes a duplicated in b         # letters in a but not in b

a | b    # all but not duplicates               # letters in a or b or both

a & b    # not duplicated                       # letters in both a and b

a ^ b                              # letters in a or b but not both

# Similarly to list comprehensions, set comprehensions are also supported:

a = {x for x in 'abracadabra' if x not in 'abc'}
a

##### 5.5. Dictionaries #####












