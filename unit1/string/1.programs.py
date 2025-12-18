
# 1️⃣ Reverse a String
# Input String: "python"
# 👉 Write a program to reverse the given string.

s="python"
s=s[::-1]
print(s)

# 2️⃣ Check Palindrome
# Input String: "madam"
# 👉 Write a program to check whether the given string is palindrome or not.

s="madam"
a=s[::-1]
if s==a:
    print("palindrome")
else:
    print("not palindrome")


# 3️⃣ Count Vowels
# Input String: "programming"
# 👉 Write a program to count the number of vowels in the given string.

s="PrOOgramming"
vowel=0
const=0
for ch in s:
    if ch.lower() in ['a','e','i','o','u']:
        vowel+=1
    else:
        const+=1
print("no of vowels",vowel)

# 4️⃣ Count Frequency of Each Character
# Input String: "banana"
# 👉 Write a program to display frequency of each character.

s="banana"
for ch in s:
    print(s.count(ch))


# 9️⃣ Replace a Word
# Input String: "I love Java"
# 👉 Write a program to replace "Java" with "Python".

s="I love Java"
s=s.replace("Java","python")
print(s)


# 1️⃣1️⃣ Count Digits, Alphabets & Special Characters
# Input String: "Python123@!"
# 👉 Write a program to count alphabets, digits, and special characters.

s="Python123@!"
alphabet=0
digits=0
special_char=0
for ch in s:
    if ch.isalpha():
        alphabet+=1
    elif ch.isdigit():
        digits+=1
    else:
        special_char+=1
print("alphabets = ",alphabet)
print("digits = ",digits)
print("special_chars = ",special_char)



# 1️⃣2️⃣ Find First and Last Occurrence
# Input String: "programming"
# Character: 'g'
# 👉 Write a program to find first and last occurrence of given character.


s="programming"
sub_string="g"
a=s.find(sub_string)
b=s.rfind(sub_string)
print("first occurence = ",a)
print("last occurence = ",b)

    
# 1️⃣3️⃣ Convert Case
# Input String: "PyThOn"
# 👉 Write a program to convert all characters to lowercase.

s="PyThOn"
s=s.lower()
print(s)

# 1️⃣4️⃣ Check String Contains Only Digits
# Input String: "2025"
# 👉 Write a program to check whether string contains only digits.

s="2025"
s.isdigit()
if s.isdigit():
    print("contain only digits")
else:
    print("does not contain digits")


# 1️⃣5️⃣ Split String into Words
# Input String: "Learning Python is fun"
# 👉 Write a program to split the string into words.

s="Learning Python is fun"
a=s.split(" ")
print(a)

# 1️⃣6️⃣ Remove Leading and Trailing Spaces
# Input String: " MCA Python "
# 👉 Write a program to remove extra spaces.

s=" MCA Python "
a=s.lstrip()
b=s.rstrip()
print(a)
print(b)


# 1️⃣7️⃣ Count Uppercase and Lowercase Letters
# Input String: "PyThOn"
# 👉 Write a program to count uppercase and lowercase letters.

s="PyThOn"
upper=0
lower=0
for ch in s:
    if ch.islower():
        lower+=1
    elif ch.isupper():
        upper+=1
print("uppercase = ",upper)
print("lowercase = ",lower)


# 9️⃣ Check Starting and Ending Characters
# Input String: "programming"
# 👉 Write a program to check whether string starts with "pro" and ends with "ing".

s="programming"
if s.startswith("pro"):
    print("string start with pro")
else:
    print("string not start with pro")


if s.endswith("ing"):
    print("string start with ing")
else:
    print("string not start with ing")