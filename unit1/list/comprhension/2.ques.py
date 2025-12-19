# 🔹 Q1. Write a Python program to find square of numbers using list comprehension

a=[x**2 for x in range(20)]
print(a)

# 🔹 Q2. Create a list of even numbers from 1 to 20 using list comprehension.

even_num=[x for x in range(1,21) if x%2==0]
print(even_num)

# 🔹 Q3. Write a program to filter odd numbers from a given list using list comprehension.
lst=[1,2,3,4,5,6,7,8,9,10]
odd_num=[x for x in lst if x%2!=0]
print(odd_num)

# 🔹 Q4. Write a program to convert all strings to uppercase using list comprehension.

lst=['abc','vaishnavi','kadam']
upper=[x.upper() for x in lst]
print(upper)

# 🔹 Q5. Write a program to find length of each word in a list using list comprehension.
lst=['abc','vaishnavi','kadam']
a=[len(x) for x in lst]
print(a)

# 🔹 Q6. Write a Python program to separate even and odd using list comprehension.
lst=[1,2,3,4,5,6,7,8,9,20,10]
even_num=[x for x in lst if x%2==0]
print(even_num)
odd_num=[x for x in lst if x%2!=0]
print(odd_num)


# 🔹 Q7. Write a program to remove vowels from a string using list comprehension.
p='education'
v=['a','e','i','o','u']
result=[ch for ch in p if ch not in v]
o=''.join(result)
print(o)

# 🔹 Q8. Write a program to create list of cubes of numbers using list comprehension.

cube_list=[x**3 for x in range(1,20)]
print(cube_list)


# 🔹 Q9. Write a program to generate pairs of numbers using nested list comprehension.

nested_list=[(x,y) for x in range(21) for y in range(20,30)]
print(nested_list)

# 🔹 Q10. Write a program to extract digits from a string using list comprehension
text='a1b2c3'
lst=[ch for ch in text if ch.isdigit()]
print(lst)

# 🔹 Q11. Write a program to reverse each string in a list using list comprehension.
lst=['vaish','kadam','vvgfd']
a=[x[::-1] for x in lst]
print(a)

# 🔹 Q12. Write a Python program to find positive numbers from a list using list comprehension.
lst=[1,2,3,4,5,-2,4,5,-4,-7]
a=[x for x in lst if x>0]
print(a)

'''que1:python code'''
animal_lst=['lion','tiger','cow','elephant','zebra']
#delete zebra from the list
animal_lst.remove('zebra')
print(animal_lst)
#print all alternate elment
print(animal_lst[::2])
#sort the list in decending order
animal_lst.sort(reverse=True)
print(animal_lst)
#add horse to the liist
animal_lst.append('horse')
print(animal_lst)


'''que2'''
input=['a','b',2,43,'Hi',900,'xyz']
op=[x for x in input if str(x).isdigit()]
print(op)

'''3'''
z=['ajay','vijay','ganesh','pareshh','mahesh']
for name in z:
    print(name[0])

# lst=[name[0] for name in z]
# print(lst)

'''4'''
# s='abcdef'
# a=" "
# for x in range(0,len(s)):
#     if





