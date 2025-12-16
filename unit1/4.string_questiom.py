# Q1.Given the string "python programming language", write a Python program to find the first 
# occurrence of the substring "gram" between valid positions. 

a="python programming language"
sub_string='gram'
b=a.find(sub_string)
if(b==-1):
    print(f"{sub_string} not found in given string")
else:
    print(f"substring {sub_string} found at index {b}")
            

# 2. Given the string "data science data analysis data", write a Python program to find the last 
# occurrence of the substring "data" in the string.

a="data science data analysis data"
sub_string='data'
b=a.rfind(sub_string)
if(b==-1):
    print(f"{sub_string} not found in given string")
else:
    print(f"substring {sub_string} found at index {b}")


# 3. Given the string "welcome to python world", write a Python program to search whether the 
# substring "python" is present in the string.
a="welcome to python world"
sub_string='python'
b=a.find(sub_string)
if(b==-1):
    print(f"{sub_string} not found in given string")
else:
    print(f"substring {sub_string} found at index {b}")

# 4. Given the string "java python java c java", write a Python program to find the last position 
# of the substring "java". 

a="java python java c java"
sub_string='java'
b=a.rfind(sub_string)
if(b==-1):
    print(f"{sub_string} not found in given string")
else:
    print(f"substring {sub_string} found at index {b}")


# 5. Given the string "abababab", write a Python program to count how many times the 
# substring "ab" appears in the string.

a="abababab"
sub_string='ab'
freq=a.count(sub_string)
print(f"frequency of given substring {sub_string} is {freq}")


''' CASE CONVERSION'''
# 6. Given the string "hello world", write a Python program to convert the entire string into 
# uppercase.
a="hello world"
result=a.upper()
print(result)


# 7. Given the string "PYTHON PROGRAMMING", write a Python program to convert the entire 
# string into lowercase. 
a="PYTHON PROGRAMMING"
result=a.lower()
print(result)

# 8. Given the string "python programming language", write a Python program to convert the 
# string so that the first letter of each word is capitalized.
a="python programming language"
result=a.title()
print(result)

# 9. Given the string "welcome to python", write a Python program to convert only the first 
# character of the string into uppercase.

a="welcome to python"
result=a.capitalize()
print(result)

# 10.  Given the string "PyThOn ProGraM", write a Python program to change uppercase letters to 
# lowercase and lowercase letters to uppercase.

a="PyThOn ProGraM"
result=a.swapcase()
print(result)


'''STRING VALIDATION'''

# 11.  Given the string "Python", write a Python program to check whether the string contains only 
# alphabetic characters.

a="Python"
b=a.isalpha()
if b:
    print(f"{a}  contains all alphabets ")
else:
    print(f"{a}  does not contains all alphabates")

# 12.  Given the string "2025", write a Python program to check whether the string contains only 
# numeric characters. 
a="2025a"
b=a.isdigit()
if b:
    print(f"{a}  contains all digits")
else:
    print(f"{a}  does not contains  all the digits")

# 13.  Given the string "hello", write a Python program to check whether all characters in the string 
# are lowercase.

a="hello"
b=a.islower()
if b:
    print(f"{a}  contains all lowercase char")
else:
    print(f"{a} does not contains lowercase char")

# 14.  Given the string "WELCOME", write a Python program to check whether all characters in the 
# string are uppercase. 
a="welcome"
b=a.isupper()
if b:
    print(f"{a}  contains all uppercase chars")
else:
    print(f"{a} does not contains uppercase chars")


# Given the string "Python123", write a Python program to check whether the string contains 
#  both letter and digits only. 
a="Python123"
b=a.isalnum()
if b:
    print(f"{a} contains both letter and digit")
else:
    print(f"{a} does not contain both letter and digit")


# ''' STRING MATCHING '''
# 16.  Given the string "python programming", write a Python program to check whether the 
# string starts with the word "python".

a="python programming"
sub_string="python"
b=a.startswith(sub_string)
if b:
    print(f"{a} string startswith {sub_string}")
else:
    print(f"{a} string does not startswith {sub_string}")


# 17.  Given the string "file_upload.pdf", write a Python program to check whether the string ends 
# with the extension ".pdf". 

a="file_upload.pdf"
sub_string=".pdf"
b=a.endswith(sub_string)
if b:
    print(f"{a} string endswith {sub_string}")
else:
    print(f"{a} string does not endswith {sub_string}")

#18.  Given the string "learning python is fun", write a Python program to check whether the 
# word "python" is present anywhere in the string.

a="learning python is fun"
sub_string="python"
b= sub_string in a
if b:
    print(f"{sub_string} is present in string")
else:
    print(f"{sub_string} is not present in string ")

# 19.  Given the strings "HelloWorld" and "helloworld", write a Python program to compare the 
# two strings ignoring case sensitivity. 

a="HelloWorld"
a=a.lower()
b="helloworld"
b=b.lower()
print(b)
if a==b:
    print(f" Both {a} and {b} are equal ignoring case")
else:
    print(f" Both {a} and {b} are not equal ignoring case")





# 20.  Given the strings "admin123" and "admin123", write a Python program to check whether 
# both strings are exactly equal.

a="admin123"
b="admin123"
if(a==b):
    print(f"both string are exactly equal")
else:
    print(f"both string are not equal")