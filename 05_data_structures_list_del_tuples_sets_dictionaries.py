
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on _________  -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


##### 5.1. More on Lists #####

# The list data type has some more methods. Here are all of the methods of 
# list objects:

# list.append(x)
  # Add an item to the end of the list. Equivalent to 
  # a[len(a):] = [x].

# list.extend(iterable)
  # Extend the list by appending all the items from the iterable. Equivalent to 
  # a[len(a):] = iterable.

# list.insert(i, x)
  # Insert an item at a given position. The first argument is the index of the 
  # element before which to insert, so a.insert(0, x) inserts at the front of the 
  # list, and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x)
  # Remove the first item from the list whose value is equal to x. It raises a 
  # ValueError if there is no such item.

# list.pop([i])
  # Remove the item at the given position in the list, and return it. If no index 
  # is specified, a.pop() removes and returns the last item in the list. 
  # (The square brackets around the i in the method signature denote that the 
  # parameter is optional, not that you should type square brackets at that position. 
  # You will see this notation frequently in the Python Library Reference.)

# list.clear()
  # Remove all items from the list. Equivalent to del a[:].

# list.index(x[, start[, end]])
  # Return zero-based index in the list of the first item whose value is equal to x. 
  # Raises a ValueError if there is no such item.

  # The optional arguments start and end are interpreted as in the slice notation 
  # and are used to limit the search to a particular subsequence of the list. 
  # he returned index is computed relative to the beginning of the full sequence 
  # rather than the start argument.

  # from the website https://www.w3schools.com/python/ref_list_index.asp

  # The index() method returns the position at the first occurrence of the 
  # specified value.

    # What is the position of the value 32:
      
      fruits = [4, 55, 64, 32, 16, 32]
      x = fruits.index(32)   # position index 3, first position found 32

# list.count(x)
  # Return the number of times x appears in the list.

# list.sort(*, key=None, reverse=False)
  # Sort the items of the list in place (the arguments can be used for sort 
  # customization, see sorted() for their explanation).

# list.reverse()
  # Reverse the elements of the list in place.

# list.copy()
  # Return a shallow copy of the list. Equivalent to a[:].

# An example that uses most of the list methods:

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'] # list
fruits.count('apple') # 2 because apple, apple in the list

fruits.count('tangerine')  # 0 because doesn't exist in the list

fruits.index('banana')  # position index 3, first position

fruits.index('banana', 4)  # Find next banana starting counting from position 4
                           # the result will be index 6

fruits.reverse()  # invert the list
fruits

fruits.append('grape')  # add 'grape' at the end
fruits

fruits.sort()   # sort the string list, it doesn't work if we have numbers and strings
fruits

fruits.pop()   # removes and shows the last item in the actual list

fruits.pop(3)  # removes and shows the item in the position 3

# You might have noticed that methods like insert, remove or sort that only modify 
# the list have no return value printed – they return the default None. 1 This is a 
# design principle for all mutable data structures in Python.

# Another thing you might notice is that not all data can be sorted or compared. 
# For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared 
# to strings and None can’t be compared to other types. Also, there are some types 
# that don’t have a defined ordering relation. For example, 3+4j < 5+7j isn’t a valid 
# comparison.


##### 5.1.1. Using Lists as Stacks #####



















