'''
Docstring for unit1.set.2.set_operations
    1.union (|): it is used to combine two sets and return new combined set
    2.intersection(&): It is used to return common elements of two set
'''

# 1.union(|)
A={1,2,3}
B={4,5,6}
C=A|B
print(C)
print(A)
print(B)

# 2.intersection(&)
A={1,2,3,4}
B={2,3,5,6}
C=A&B
print(C)

# 3.difference(-):
A={11,12,13,14}
B={12,13,18,20}
C=A-B
D=B-A
print(C)
print(D)

# 4.symmetric difference(^)
A={11,12,13,14}
B={12,13,18,20}
print(A^B)

# 5.subset
A={1,2,3,4}
B={1,2,3,4,5,6,7}
print(A<=B)

# 6.Proper subset(<)
A={1,2,3,4}
B={1,2,3,4}
print(A<B) #False as A is subset of B but it is equla so it return false
A={1,2,3,4}
B={1,2,3,4,5,6}
print(A<B) # True (As A is Subset of B and A and B are not equal so it returns True )


# 7.superset(>=,>)
A={1,2,3,4}
B={1,2,3,4}
print(A>B)
print(A>=B)




