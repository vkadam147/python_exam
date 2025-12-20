'''
    Dictionary:
        1.It is an unordered  collection  where data is stored in the form of key:value pair which is mutable
        2.In dictionary keys are always unique and immutable
        3.In dictionary values can be heterogeneous and mutable
'''

d={1:'one',2:'two',3:'three',4:'four',5:'five'}
d[6]='six'
print(d)
a=d.pop(1)
print(d)
print(a)
d[3]='thirty'
print(d)

for key in d.keys():
    print(key,d[key])

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)


d={1:'one',2:'two',3:'three',4:'four',5:'five'}


b=d.popitem()
print(d)
print(b)

del d[3]
print(d)

d.clear()
print(d)





#creating dictionary

a={1:'one',2:'Two',3:'Three'}

# accessing  using a[key]
print(a[1]) #one
print(a[2]) #two
print(a[3]) #three
# print(a[4]) # Raises an keyError as key 4 is not present in dictionary

#accessing using get() method
print(a.get(1))  #one
print(a.get(2)) # two
print(a.get(3)) # three
print(a.get(4)) # None it will not raise any keyerror it just return None


# remove using dict.pop(key)
removed_value=a.pop(1)
print(f"Removed Value:{removed_value}")
print(f"Newly updated dict:{a}")
# z=a.pop(5) # as key 5 is not present in dictionary so it raise KeyError


# removed using popitem(): it removes last added pair and returns in tuple
removed_key_value=a.popitem()
print(f"Removed Key Value Pair:{removed_key_value} type is {type(removed_key_value)}")
key,value=removed_key_value
print(f"Key:{key} Value:{value}")

# using del dict[key]

del a[2]
print(a)

#clear():It renoves all entries from dictionary
a.clear()





