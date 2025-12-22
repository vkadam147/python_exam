# # my_dict={1:'One',2:'Two',3:'Three'}
# # print(my_dict.keys())
# # a=my_dict.keys()
# # print(a)


# # # 10 names input
# # name1=input("Enter First name")
# # name2=input("Enter First name")
# # name3=input("Enter First name")
# # name4=input("Enter First name")
# # name5=input("Enter First name")
# # name6=input("Enter First name")
# # name7=input("Enter First name")
# # name8=input("Enter First name")

# # s=set()
# # for i in range(5):
# #     name=input(f'Enter {i} Name')
# #     s.add(name)
# # print(s)


# n=int(input("enter a no of elements"))
# s=set()
# for x in range(n):
#     name=input("enter a elements (0-9 or A-Z or a-z)")
#     if name.isalnum():
#         s.add(name)


# #display the set elements 
# for name in s:
#     print(name)

# #lenngth of set
# print(f"lenghth of set:{len(s)}")

# #count
# digit=0
# lower=0
# upper=0

# for name in s:
#     for ch in name:
#         if ch.isdigit():
#             digit+=1
#         elif ch.islower():
#             lower+=1
#         elif ch.isupper():
#             upper+=1
# print(f"no of digits:{digit}")
# print(f"no of uppercase char:{upper}")
# print(f"no of lowercase char:{lower}")


# #dictionary
# #creating a dictionary

# my_dict={1:'one',2:'two',3:'three',4:'four',5:'five'}

# #to display all thr keys
# for keys in my_dict.keys():
#     print(keys)

# #add new key value pair
# my_dict[6]='six'
# print(my_dict)

# #delete specific element 
# element=4
# removed_element=my_dict.pop(element)
# print(removed_element)
# print(my_dict)

# #modify vale
# my_dict[3]='thirty'
# print(my_dict)

# print("=============================================================================================")

# input_list=['Ajay','Vijay','Ganesh','Paresh','Mahesh']
# output_list=[word[0] for word in input_list ]
# print(output_list)


# animals=['lion','tiger','cow','elephant','zebra']

# #delete
# animals.remove('zebra')
# print(animals)

# #alternate element
# print(animals[::2])

# #sort
# animals.sort(reverse=True)
# print(animals)

# #add
# animals.append('horse')
# print(animals)


# input_list=['a','b',2,43,900,'xyz']
# output_list=[x for x in input_list if str(x).isdigit()]
# print(output_list)


n=int(input("enter a elements:"))
s=set()
for name in range(n):
    name=input("enter a name (o-9 or A-Z or a-z):")
    if name.isalnum():
        s.add(name)
    
for name in s:
    print(name)

#length
print(f"length of set:{len(s)}")

#count
digit=0
lower=0
upper=0

for x in s:
    for ch in x:
        if ch.isdigit():
            digit+=1
        elif ch.isupper():
            upper+=1
        elif ch.islower():
            lower+=1

print(f"no of digits:{digit}")
print(f"no of uppercaase char:{upper}")
print(f"no of lowercase char:{lower}")
