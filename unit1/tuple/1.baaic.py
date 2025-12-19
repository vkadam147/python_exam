'''
Docstring for unit1.tuple.1.baaic


1.Tuple is an indexed collection of heterogeneous elements which is immutable stored in single variable
    1.ordered
    2.indexed
    3.immutable
    4.heterogeneous
    5.allowed duplicates

2. How to create tuple?
    1.using () round brackets
    2.using constructor
        t=tuple(iterable)
                iterbale:
                    1.list
                    2.string
                    3.set
3.Tuple packing and unpacking:
    a.Tuple packing:
        it is the process of storing multiple values in single variable seperated dby comma
        a=1,2,3,4,5,6
        a----><class tuple>
    b.tuple unpacking:
        It is the process of assigning values from tuple to multiple variables
    
    c.Extended Unacking:
        if we want to unpack some values of tuple to variable and remaining all in to single variable then extended unpacking comes
        1.In extended unpacking remaining all values stored as list
        Rules:
            a.Only one * variable allowed in extended unpacking multiple * varibale will leads to an error
                *a,*b,c=t   =====>leads to an error
            b.* variable always stored as list
            c.Remaining variables must get values otherwise we will get an error
                a,*b,c=(1,2)======>get error
            d.we can not use single * variable 
    
    d.List extended unpacking:
        It will work same as tuple
        a,*b,c=[1,2,3,4,5]
        a=1
        b=[2,3,4]
        c=5

Operations on Tuple:
    1.concatenation:(+)
        It is used   to join two tuple and it will always return new tuple
        It will not modify orignal tuple as tuple is immutable
    2.Repetition(*):
        It is used to repeat tuple elements n times
        It will not modify orignal tuple as tuple is immutable
    3.Membership Operator:
        IN: It is used to verify whether given element present in tuple or not
                returns True: If given element present in tuple
                return False: if given element not present in tuple
        
        NOT IN: It is used to verify whether given element not present in tuple 
                returns True: If given element not present in tuple
                return False: if given element present in tuple
    4.Relational Operators:
        1(==):
            double equals (==) operator is used for content comparion of two tuples
        2.(>,<,>=,<=,!=):
           It always compares two tuples lexiographocally
    5.Indentity Operator:(IS ,NOT IS):
        1.Is:
            a.It is used to compare two tuples based on address
            b.It will return True if two  references are pointing to same tuple object
            c.It will return fasle if two references are not pointing to same tuple object
        2.Is NOT:
            a.It is used to compare two tuples based on address
            b.It will return True if two  references are not pointing to same tuple object
            c.It will return fasle if two references are  pointing to same tuple object
    6.Logical Operator(and or not):
        1.empty tuple always returns false
        2.Non empty tuple always return True

Tuple methods:
    1.As tuple is immutable in nature it supports only 2 methods
            1.tuple.count(element):
                It will return the occurence of given element from the element
            2.tuple.index(element):
                It will return the index of given element
Built in functions:
    1.max(tuple): It will return the maximum element from tuple
    2.min(tuple):It will return the minimum element from tuple
    3.sum(tuple):It will return the sum of all elements of sum
    4.sorted(tuple): It will sort the tuple elements and return the list
    5.len(tuple):It will return the length of tuple

'''

# using round brackets
t=(1,2,3)
print(t)

# using constructor

# string to tuple conversion
t=tuple('python')
print(t)
print(type(t))

#list to tuple
nums_list=[1,8,2,4,2,5]
t=tuple(nums_list)
print(t)
print(type(t))

# set to tuple
s={1,2,3,4,5,6}
t=tuple(s)
print(t)
print(type(t))

# dictionary to tuple
my_dict={101:'Java',102:'Python',103:'C++'}
t=tuple(my_dict)
print(t)
print(type(t))



# Tuple packing
a=1,2,3,4
print(a)
print(type(a))

# tuple unpacking
t=(1,2,None,'java',True)
a,b,c,d,e=t
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))


# extended unpacking
t=(9,5,2,9,1,3,4,1,2,2)
a,b,*c=t
print(a,type(a))
print(b,type(b))
print(c,type(c))

*p,q,r=t
print(p)
print(q)
print(r)


x,*y,z=t
print(x)
print(y)
print(z)


# list extended unpacking
l=[1,2,3,4,5]
a,*b,c=l
print(a)
print(b)
print(c)


# creating an empty tuple
a=(1) # it will not create tuple it just create an int object
print(a,type(a))

# to create single valye tuple
a=(1,)
print(a,type(a))
b=2,
print(b,type(b))
# c=tuple(1,)
# print(c)


# Relational operator
t1=(1,2,3)
t2=(1,2,3)
print(t1==t2)

t1=(1,2,3,4)
t2=(1,2,3,5)
print(t1>t2)
print(t1<t2)


# identity operator (Is,Is Not): verifies addresses of two tuples
a=(1,2,3)
b=1,2,3
print(a is b)
print(a is not b)


#logical operators:
print("----------------------------------------------")
a=()
b=(1,2)
print(bool(a)) #False
print(bool(b)) # True
print(a  and b) #False---->()
print(a or b)#True--->(1,2)
print( not a)#True
print(not b)#False


# Tuple methods

s=(9,5,2,9,1,3,4,1,2,2)
print(s.count(2))
print(s.index(1))

#buit in method

num_tuple=(1,2,3,10,-2,-4,200)
#1]len(tuple)
a=len(num_tuple)
print(a)

#2]max(tuple)
b=max(num_tuple)
print(b)

#3]min(tuple)
c=min(num_tuple)
print(c)

#4]sum(tuple)
d=sum(num_tuple)
print(d)

#5]sorted(tuple)
e=sorted(num_tuple)
# e.reverse()
print(e)


print("-----------------Built in functions-------------------------------------")
t=(1,8,2,4,2,5)
print(f"Maximum Element Of Tuple is {max(t)}")
print(f"Minimum Elemenr of tuple is {min(t)}")
print(f"Sum of Tuple elements is : {sum(t)}")
print(f"Length of tuple is {len(t)}")
print(f"Sorted Tuple in the form of list is {sorted(t)}")












