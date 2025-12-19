# 🔹 Q1. Write a Python program to find square of numbers using list comprehension.

a=[1,2,3,4,5,6]
b=[x**2  for x in a]
print(b)

c=[x for x in range(20)]
print(c)

# 🔹 Q2. Create a list of even numbers from 1 to 20 using list comprehension.

even_num=[x for x in range(1,21) if x%2==0]
print(even_num)

# 🔹 Q3. Write a program to filter odd numbers from a given list using list comprehension.

nums = [10, 15, 20, 25, 30]
odd_num=[x for x in nums if x%2!=0]
print(odd_num)

# 🔹 Q4. Write a program to convert all strings to uppercase using list comprehension.

l=['python','java','c','pascal','pojo','patient']
p=[x.upper() for x in l]
s=[x.upper() for x in l if x.startswith('p')]
print(p)
print(s)

# Q5. Write a program to find length of each word in a list using list comprehension.
l=['python','java','c','pascal','pojo','patient']
a=[len(x) for x in l]
print(a)


a=[1,2,3,1,1,1,1,8,9,10]
l=['Even' if x%2==0 else 'Odd' for x in a]
print(l)