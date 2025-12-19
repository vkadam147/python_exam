"""
PYTHON TUPLE COMPLETE NOTES (UNIT 1)
"""

# ---------------------------------------------------------
# 1. WHAT IS A TUPLE?
# ---------------------------------------------------------
# Tuple is an indexed collection of heterogeneous elements
# which is immutable and stored in a single variable.
#
# Properties:
# 1. Ordered
# 2. Indexed
# 3. Immutable
# 4. Heterogeneous
# 5. Allows duplicate elements

t = (1, "Python", True, 3.5, 1)
print(t)


# ---------------------------------------------------------
# 2. CREATING A TUPLE
# ---------------------------------------------------------

# 2.1 Using round brackets
t1 = (1, 2, 3)
print(t1)

# 2.2 Using tuple() constructor

# String to tuple
t2 = tuple("python")
print(t2)

# List to tuple
lst = [1, 8, 2, 4, 2, 5]
t3 = tuple(lst)
print(t3)

# Set to tuple (order not guaranteed)
s = {1, 2, 3, 4}
t4 = tuple(s)
print(t4)

# Dictionary to tuple (keys only)
d = {101: "Java", 102: "Python"}
t5 = tuple(d)
print(t5)


# ---------------------------------------------------------
# 3. TUPLE PACKING AND UNPACKING
# ---------------------------------------------------------

# 3.1 Tuple Packing
# Storing multiple values into a single tuple variable
a = 1, 2, 3, 4
print(a, type(a))

# 3.2 Tuple Unpacking
t = (1, 2, None, "Java", True)
a, b, c, d, e = t
print(a, b, c, d, e)

# 3.3 Extended Unpacking
# Remaining values are stored in a LIST
t = (9, 5, 2, 9, 1, 3, 4, 1, 2, 2)

x, y, *z = t
print(x, y, z)

*p, q, r = t
print(p, q, r)

x, *y, z = t
print(x, y, z)

# Rules:
# 1. Only one * variable allowed
# 2. * variable always stores values in a list
# 3. Remaining variables must get values
# 4. Single * variable is not allowed


# ---------------------------------------------------------
# 4. LIST EXTENDED UNPACKING (SAME AS TUPLE)
# ---------------------------------------------------------
lst = [1, 2, 3, 4, 5]
a, *b, c = lst
print(a, b, c)


# ---------------------------------------------------------
# 5. SINGLE ELEMENT TUPLE
# ---------------------------------------------------------

a = (1)       # Not a tuple
print(a, type(a))

b = (1,)      # Tuple with one element
print(b, type(b))

c = 2,
print(c, type(c))


# ---------------------------------------------------------
# 6. OPERATIONS ON TUPLE
# ---------------------------------------------------------

# 6.1 Concatenation (+)
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)

# 6.2 Repetition (*)
print(t1 * 3)

# 6.3 Membership Operators
print(2 in t1)
print(5 not in t1)


# ---------------------------------------------------------
# 7. RELATIONAL OPERATORS
# ---------------------------------------------------------

t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 == t2)   # Content comparison

t3 = (1, 2, 4)
print(t1 < t3)    # Lexicographical comparison


# ---------------------------------------------------------
# 8. IDENTITY OPERATORS (is, is not)
# ---------------------------------------------------------

t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(id(t1))
print(id(t2))

print(t1 == t2)   # True (same content)
print(t1 is t2)   # May be True or False

# NOTE:
# Python may optimize memory by reusing immutable objects,
# so small tuples can sometimes have the same id.
# Never use 'is' for content comparison.


# ---------------------------------------------------------
# 9. LOGICAL OPERATORS
# ---------------------------------------------------------

a = ()
b = (1, 2)

print(bool(a))    # False
print(bool(b))    # True

print(a and b)    # ()
print(a or b)     # (1, 2)
print(not a)      # True
print(not b)      # False


# ---------------------------------------------------------
# 10. TUPLE METHODS
# ---------------------------------------------------------

# Tuples support only 2 methods because they are immutable

t = (9, 5, 2, 9, 1, 3, 4, 1, 2, 2)

# 10.1 count()
print(t.count(2))

# 10.2 index()
print(t.index(1))


# ---------------------------------------------------------
# 11. BUILT-IN FUNCTIONS ON TUPLE
# ---------------------------------------------------------

num_tuple = (1, 2, 3, 10, -2, -4, 200)

print(len(num_tuple))      # Length
print(max(num_tuple))      # Maximum
print(min(num_tuple))      # Minimum
print(sum(num_tuple))      # Sum
print(sorted(num_tuple))   # Sorted list
avg=sum(t)/len(t)
print(avg)

print("------ END OF TUPLE NOTES ------")
