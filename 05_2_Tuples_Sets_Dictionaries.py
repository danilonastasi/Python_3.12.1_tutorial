
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on 01/15/2024  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


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

# Another useful data type built into Python is the dictionary 
# (see Mapping Types — dict). Dictionaries are sometimes found in other 
# languages as “associative memories” or “associative arrays”. Unlike 
# sequences, which are indexed by a range of numbers, dictionaries are indexed 
# by keys, which can be any immutable type; strings and numbers can always be 
# keys. Tuples can be used as keys if they contain only strings, numbers, or 
# tuples; if a tuple contains any mutable object either directly or indirectly, 
# it cannot be used as a key. You can’t use lists as keys, since lists can be 
# modified in place using index assignments, slice assignments, or methods 
# like append() and extend().

# It is best to think of a dictionary as a set of key: value pairs, with the 
# requirement that the keys are unique (within one dictionary). A pair of 
# braces creates an empty dictionary: {}. Placing a comma-separated list of 
# key:value pairs within the braces adds initial key:value pairs to the 
# dictionary; this is also the way dictionaries are written on output.

# The main operations on a dictionary are storing a value with some key and 
# extracting the value given the key. It is also possible to delete a key:value 
# pair with del. If you store using a key that is already in use, the old value 
# associated with that key is forgotten. It is an error to extract a value 
# using a non-existent key.

# Performing list(d) on a dictionary returns a list of all the keys used in the 
# dictionary, in insertion order (if you want it sorted, just use 
# sorted(d) instead). To check whether a single key is in the dictionary, 
# use the in keyword.

# Here is a small example using a dictionary:

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127   # new assignment to the dictionary
tel

tel['jack']   # 'jack' is the key, I call the key an I get the value

del tel['sape']   # I remove key 'sape' and his value
tel['irv'] = 4127    # adding new key and value
tel

list(tel)   # it shows just the keys

sorted(tel)    # sort the keys

'guido' in tel

'jack' not in tel

# The dict() constructor builds dictionaries directly from sequences of key-value 
# pairs:

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# In addition, dict comprehensions can be used to create dictionaries from 
# arbitrary key and value expressions:

{x: x**2 for x in (2, 4, 6)}

# When the keys are simple strings, it is sometimes easier to specify pairs using 
# keyword arguments:

dict(sape=4139, guido=4127, jack=4098)


##### 5.6. Looping Techniques #####

# When looping through dictionaries, the key and corresponding value can be 
# retrieved at the same time using the items() method.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding value 
# can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be 
# paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):  # zip can associate index 0 in both 
                                # sequences together. The same index 1,1 and 2,2
    print('What is your {0}?  It is {1}.'.format(q, a))  # postiion 1 will be the 
                                               # index 1 of the new zip sequence

# To loop over a sequence in reverse, first specify the sequence in a forward 
# direction and then call the reversed() function.

for i in reversed(range(1, 10, 2)):
    print(i)

# To loop over a sequence in sorted order, use the sorted() function which 
# returns a new sorted list while leaving the source unaltered.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Using set() on a sequence eliminates duplicate elements. The use of sorted() in 
# combination with set() over a sequence is an idiomatic way to loop over unique 
# elements of the sequence in sorted order.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# It is sometimes tempting to change a list while you are looping over it; 
# however, it is often simpler and safer to create a new list instead.

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data   # nan values are removed


##### 5.7. More on Conditions #####

# The conditions used in while and if statements can contain any operators, not 
# just comparisons.

# The comparison operators in and not in are membership tests that determine 
# whether a value is in (or not in) a container. The operators is and is not 
# compare whether two objects are really the same object. All comparison 
# operators have the same priority, which is lower than that of all numerical 
# operators.

# Comparisons can be chained. For example, a < b == c tests whether 
# a is less than b and moreover b equals c.

# Comparisons may be combined using the Boolean operators and and or, and the 
# outcome of a comparison (or of any other Boolean expression) may be negated 
# with not. These have lower priorities than comparison operators; between them, 
# not has the highest priority and or the lowest, so that A and not B or C is 
# equivalent to (A and (not B)) or C. As always, parentheses can be used to 
# express the desired composition.

# The Boolean operators and and or are so-called short-circuit operators: their 
# arguments are evaluated from left to right, and evaluation stops as soon as 
# the outcome is determined. For example, if A and C are true but B is false, 
# A and B and C does not evaluate the expression C. When used as a general 
# value and not as a Boolean, the return value of a short-circuit operator is 
# the last evaluated argument.

# It is possible to assign the result of a comparison or other Boolean 
# expression to a variable. For example,

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3  # it is assigned the firts value not null
non_null

# Note that in Python, unlike C, assignment inside expressions must be done 
# explicitly with the walrus operator :=. This avoids a common class of problems 
# encountered in C programs: typing = in an expression when == was intended.


##### 5.8. Comparing Sequences and Other Types #####

# Sequence objects typically may be compared to other objects with the same 
# sequence type. The comparison uses lexicographical ordering: first the first 
# two items are compared, and if they differ this determines the outcome of the 
# comparison; if they are equal, the next two items are compared, and so on, 
# until either sequence is exhausted. If two items to be compared are themselves 
# sequences of the same type, the lexicographical comparison is carried out 
# recursively. If all items of two sequences compare equal, the sequences are 
# considered equal. If one sequence is an initial sub-sequence of the other, 
# the shorter sequence is the smaller (lesser) one. Lexicographical ordering 
# for strings uses the Unicode code point number to order individual characters. 
# Some examples of comparisons between sequences of the same type:

(1, 2, 3)              < (1, 2, 4)  # True
[1, 2, 3]              < [1, 2, 4]  # True
'ABC' < 'C' < 'Pascal' < 'Python'   # True 
'DCB' < 'C' < 'Pascal' < 'Python'   # False, I think because DCB comes after C 
                                    # in the alphabet
(1, 2, 3, 4)           < (1, 2, 4)  # True  because 3 < 4 index 2
(1, 2)                 < (1, 2, -1) # True  because 1=1 ,2=2 but the first list 
                                    # is less lenght than the second
(1, 2, 3)             == (1.0, 2.0, 3.0)   # True
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)  # True

# Note that comparing objects of different types with < or > is legal provided 
# that the objects have appropriate comparison methods. For example, mixed numeric 
# types are compared according to their numeric value, so 0 equals 0.0, etc. 
# Otherwise, rather than providing an arbitrary ordering, the interpreter will 
# raise a TypeError exception.




