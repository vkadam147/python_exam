natural_num={x for x in range(1,21)}
 
for num in natural_num:
    print(num)


l=[x for x in range(100)]
even_num={x for x in l if x%2==0}
print(even_num)


s="programming"
a={x for x in s}
print(a)

t=(True,False,True,False)
x={1 if a else 0 for a in t}
print(x)


t=(18,24,25)
a={x**2 for x in t}
print(a)

s="i love python"
vowels={'a','e','i','o','u'}
a={x for x in s if x in 'aeiou'}
print(a)