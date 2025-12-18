
'''
1.Case methods

'''
'''
1.string.upper():# This will return the new string in upper case characters
'''
a='python'
a=a.upper()
print(a) 

'''-----------------------------------------------------------------------------------'''


'''
2.string.lower():# This will return the new string in lower case characters
'''
a='PYTHON'
a=a.lower()
print(a) 
'''-----------------------------------------------------------------------------------'''



'''
3.string.title():This method converts the first character of each word in the string into
uppercase
'''
a='python is easy language'
a=a.title()
print(a) 
'''-----------------------------------------------------------------------------------'''


'''
4.string.capitalize():This method converts the first character of first word in the string into
uppercase
'''
a='python is easy language'
a=a.capitalize()
print(a) 

'''-----------------------------------------------------------------------------------'''



'''
5.string.swapcase():This method changes uppercase letters to lowercase and lowercase to uppercase
'''
a='pytHon Is Easy lAnguage'
a=a.swapcase()
print(a) 

'''=====================================================================================
======================================================================================='''

'''' 2.Searching & Counting Methods'''

'''
1.s.find(sub[, start[,end]]):This method searches for a substring and returns its index position. If the substring is not found, it returns -1.
'''
a="python is easy language"
sub_string="easy"
b=a.find(sub_string)
if(b==-1):
    print(f"{sub_string} not found in given string")
else:
    print(f"substring {sub_string} found at index {b}")

'''-----------------------------------------------------------------------------------'''


'''
2.s.rfind(sub[,start[, end]]):This method searches for a substring from the right side of the string
'''
a="python is easy language easy"
sub_string="easy"
b=a.rfind(sub_string)
if(b==-1):
    print(f"{sub_string} not found in given string")
else:
    print(f"substring {sub_string} found at index {b}")

'''-----------------------------------------------------------------------------------'''


'''
3. s.index(sub[,start[, end]]):This method returns the index of the substring but raises an error if the substring is not found
'''
a="python is easy language"
sub_string="is"
b=a.index(sub_string)
if(b==-1):
    print(f"{sub_string} not found in given string")
else:
    print(f"substring {sub_string} found at index {b}")

'''-----------------------------------------------------------------------------------'''


'''
4. s.rindex(sub[,start[, end]]):This method returns the index from the right side of the substring but raises an error if the substring is not found
'''
a="python is easy language easy"
sub_string="easy"
b=a.rindex(sub_string)
if(b==-1):
    print(f"{sub_string} not found in given string")
else:
    print(f"substring {sub_string} found at index {b}")

'''-----------------------------------------------------------------------------------'''


'''
5.s.count(sub[,start[, end]]) : This method returns the total number of occurrences of a substring in the string.
'''
a="python is easy language easy python"
sub_string="python"
b=a.count(sub_string)
print(f"frequency of given substring is {b}")

''''====================================================================================='''


'''3.Checking / Validation Methods'''

'''
1.s.isalpha():Returns True if the string contains only alphabets and no digits or spaces.

'''
a="python is easy language"
b=a.isalpha()
if b:
    print(f"{a} contain all alphabets")
else:
    print(f"{a} does not conntain all alphabets ")

'''--------------------------------------------------------------------------------------'''

'''
2.s.isdigit():Returns True if the string contains only digits.
'''
a="9529134122"
b=a.isdigit()
if b:
    print(f"{a} contain all digits")
else:
    print(f"{a} does not conntain all the digits ")

'''--------------------------------------------------------------------------------------'''













'''5.Splitting & Joining'''

sentence='Python-is-easy-and-python-is-funny'
list_sentence=sentence.split('-')
print(f"List Sequence:{list_sentence}")



sen=''' 
This is 

python language

mongo db 

django

'''

l=sen.splitlines()
print(l)




