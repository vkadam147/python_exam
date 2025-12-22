# d1={101:'Java',102:'Python'}
# l={[103,'cloud'],[104,'Web']}
# print(d1)

# d1.update(l)
# print(d1)
# l=[1,2,3,4]
# l1=[1,2,3,4]
# l2=[1,2,3,4]
# s={l,l1,l2}
# print(s)

names=['vaishnavi','Manavi','Sanskriti']
print(f"Address of list names  is{id(names)}")
print('----------------------------------------------------------')
d={'name':names,'roll_no':326}
print(f"Dictionary d is {d}")
d_copy=d.copy()
d['roll_no']=252
print(f"Dictionary d after update is {d}")
print(f"Address of d is {id(d)}")
name_list=d['name']
print(f"name list is {name_list}")
print(f"Address of name_lis is{id(name_list)}")
print('----------------------------------------------------------')




print(f"Dictionary d_copy is {d_copy}")
print(f"Address of d_coppy is {id(d_copy)}")
copy_name_list=d_copy['name']
print(f"copy name list is {copy_name_list}")
print(f"Address of copy name list is {id(copy_name_list)}")
print('----------------------------------------------------------')


names.append('Renu')
print(d)
print(d_copy)








