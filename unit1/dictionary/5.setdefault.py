# marks={}
# l=[]
# print(f"Address of created list L:{id(l)}")
# list_marks=marks.setdefault('Mathematics',l)
# print(f"Address of list:{id(list_marks)}")
# print(f"marks before updating list:{marks}")
# list_marks.append(89)
# list_marks.append(99)
# print(list_marks)
# print(f"marks after updating list:{marks}")
# print(marks)
# print(f"Address of Inner Object as Value:{id(marks['Mathematics'])}")


a='immutablaaae'
dict_one={}
for ch in a:
    dict_one.setdefault(ch,0)
    l,c