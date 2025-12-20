'''python provide buit in method :
        1.method for adding element:
          a.add():it is used to add single element to set
                    syntax: set.add(element)


          b.update():update(iterable) method is used to add multiple element from another iterable
                        1.element are added one by one from given iterable
                        2.iterable are:
                            a.list
                            b.tuple
                            c.set
                            d.string
                        2.duplicate values are ignored
                            SYNTAX: set.update(iterable)

         2.methods for removing elements:
            a.remove():
                1.remove(element) method is used to remove specific element from set
                2.if element not found it raises an error
                    syntax: set.remove(element)

            b.discard():
                1.discard(element) method is used to remove specific element from set
                2.discard()method will not raise error if element not found
                    syntax:set.discard(element)

            c.pop():
                1.it is used to remove and return random elemennt from set
                2.set is unorderd so pop() method can remove and return only random element from set
                    syntax:set.pop()
            
            d.clear():
                1.it is used to remove all elements from set
                2.after calling clear() method set becomes empty
                    syntax:set.clear()
                      
'''


#1. add() method
s = {1, 2, 3}
s.add(4)
print(s)

# 2. update() method
print("2. update() method")
s = {1, 2}
s.update([2, 3, 4])
print(s)


# 3. remove() method
print("3. remove() method")
s = {10, 20, 30}
s.remove(20)
print(s)


# 4. discard() method
print("4. discard() method")
s = {5, 10, 15}
s.discard(10)
print(s)


# 5. pop() method
print("5. pop() method")
s = {100, 200, 300}
x = s.pop()
print("Popped element:", x)
print("Remaining set:", s)
print("-" * 30)

# 6. clear() method
print("6. clear() method")
s = {1, 2, 3, 4}
s.clear()
print(s)
