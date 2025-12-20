# '''
# Docstring for unit1.set.2.set_operations
#     1.union (|): it is used to combine two sets and return new combined set
#     2.intersection(&): It is used to return common elements of two set
# '''

# # 1.union(|)
# A={1,2,3}
# B={4,5,6}
# C=A|B
# print(C)
# print(A)
# print(B)

# # 2.intersection(&)
# A={1,2,3,4}
# B={2,3,5,6}
# C=A&B
# print(C)

# # 3.difference(-):
# A={11,12,13,14}
# B={12,13,18,20}
# C=A-B
# D=B-A
# print(C)
# print(D)

# # 4.symmetric difference(^)
# A={11,12,13,14}
# B={12,13,18,20}
# print(A^B)

# # 5.subset
# A={1,2,3,4}
# B={1,2,3,4,5,6,7}
# print(A<=B)

# # 6.Proper subset(<)
# A={1,2,3,4}
# B={1,2,3,4}
# print(A<B) #False as A is subset of B but it is equla so it return false
# A={1,2,3,4}
# B={1,2,3,4,5,6}
# print(A<B) # True (As A is Subset of B and A and B are not equal so it returns True )


# # 7.superset(>=,>)
# A={1,2,3,4}
# B={1,2,3,4}
# print(A>B)
# print(A>=B)


# #8.Membership test operator:
# A={1,2,3,4}
# print(f"4 in A:{4 in A}") #True
# print(f"5 in A:{5 in A}") #False

# print(f"5 NOT In A:{5 not in A}") # True
# print(f"4 NOT In A:{4 not in A}") # False


# #9.Identity Operator
# A={1,2,3}
# B={1,2,3}
# C=A
# print(f"A is B: {A is B}")
# print(f"C is A :{C is A}")
# print(f"B is not C:{B is not C}")

'''
Docstring for unit1.set.2.set_operations

SET OPERATIONS & OPERATORS (FROM SCRATCH)

1. union (|)
   • Used to combine all elements of two sets
   • Duplicate elements are removed automatically
   • Returns a NEW set
'''
# 1. union (|)
A = {1, 2, 3}
B = {4, 5, 6}
C = A | B
print(C)     # {1, 2, 3, 4, 5, 6}
print(A)     # Original set remains unchanged
print(B)

'''
2. intersection (&)
   • Used to find common elements between two sets
   • Returns a NEW set containing only common values
'''
# 2. intersection (&)
A = {1, 2, 3, 4}
B = {2, 3, 5, 6}
C = A & B
print(C)     # {2, 3}

'''
3. difference (-)
   • Returns elements present in first set but not in second
   • Order: A - B ≠ B - A
'''
# 3. difference (-)
A = {11, 12, 13, 14}
B = {12, 13, 18, 20}
C = A - B
D = B - A
print(C)     # {11, 14}
print(D)     # {18, 20}

'''
4. symmetric difference (^)
   • Returns elements that are NOT common in both sets
   • Common elements are removed
'''
# 4. symmetric difference (^)
A = {11, 12, 13, 14}
B = {12, 13, 18, 20}
print(A ^ B) # {11, 14, 18, 20}

'''
5. subset (<=)
   • Returns True if all elements of A are present in B
'''
# 5. subset (<=)
A = {1, 2, 3, 4}
B = {1, 2, 3, 4, 5, 6, 7}
print(A <= B)    # True

'''
6. proper subset (<)
   • A is a proper subset of B if:
     - All elements of A are in B
     - A and B are NOT equal
'''
# 6. proper subset (<)
A = {1, 2, 3, 4}
B = {1, 2, 3, 4}
print(A < B)     # False (both sets are equal)

A = {1, 2, 3, 4}
B = {1, 2, 3, 4, 5, 6}
print(A < B)     # True

'''
7. superset (>= , >)
   • Superset contains all elements of another set
   • >= allows equality
   • > means proper superset
'''
# 7. superset (>= , >)
A = {1, 2, 3, 4}
B = {1, 2, 3, 4}
print(A > B)     # False
print(A >= B)    # True

'''
8. Membership operators (in, not in)
   • Used to check presence or absence of element in set
   • Fast operation because set uses hashing
'''
# 8. Membership test operator
A = {1, 2, 3, 4}
print(f"4 in A : {4 in A}")        # True
print(f"5 in A : {5 in A}")        # False
print(f"5 not in A : {5 not in A}")# True
print(f"4 not in A : {4 not in A}")# False

'''
9. Identity operators (is, is not)
   • Checks whether two variables refer to SAME memory object
   • Not used to compare values
'''
# 9. Identity operator
A = {1, 2, 3}
B = {1, 2, 3}
C = A

print(f"A is B : {A is B}")        # False (different objects)
print(f"C is A : {C is A}")        # True (same reference)
print(f"B is not C : {B is not C}")# True






