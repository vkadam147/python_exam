'''
Dictionary Comprehension:
    1.It is a way of creating an dictionary in single line 

'''

# create a dictionary of numbers with key as int and value as string

my_dict={num:str(num)for num in range(11)}
print(my_dict)
for key in my_dict.keys():
    print(key,my_dict[key])

#ceate a dictionary of first 10 natural numbers with its squares

my_dict={num:num**2 for num in range(1,11)}
for key,value in my_dict.items():
    print(key,value)

#even no
my_dict={num:'even' for num in range(1,11) if num%2==0}
print(my_dict)

my_dict={num:'even' if num%2==0 else 'odd' for num in range(1,11)}
print(my_dict)


college='ssssssssssssssssssssssssssssssssssssssssssssssinhgaads'
frequnecy={ch:college.count(ch) for ch in college}
print(frequnecy)