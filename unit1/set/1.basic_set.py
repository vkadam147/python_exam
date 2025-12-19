'''

SET:
    1.set is an unordered collection of heterogeneous elements stored in single variable where duplicates are not allowed and which is mutable
 key Properties:
    1.unordered: Can not be accessed using index
    2.mutable: can be changed and modifiable
    3.heterogeneous: set can have different type of elements
    4.duplicates not allowed: set can contain only unique elements

    creating set:
        1.using curly braces:{}
            we can create set  directly using curly braces:
                a={1,2,3}
                s={} =====>this is not set this is dictionary
            To create empty set:
                s=set()
        2.using constructor:
            1.we can create set using constructor which can be used for type conversion also
                s=set(iterable)
                    iterable:
                        1.list
                        2.string
                        3.tuple
            2.we can create empty set using constructor only
                empty_set=set()
    Accessing set:
        1.we can access set only using loop
        2.we can not access set using indices as set is an unordered
'''



'''using curly braces'''
s={10,20,30,40}
print(s,type(s))

'''2]using constructor'''
a=set()
print(a)

#list to set
b=set([1,2,3])
print(b)

#tuple to set
c=set((1,2,3,4))
print(c)

#dic to set
d=set({1:'one',2:'two',3:'three'})
print(d)

'''3]accessing element of set'''
# set_num[0]====>we can not access set using indices as set in unorderd
set_num={1,2,3,4,5,6}
for num in set_num:
    print(num)
