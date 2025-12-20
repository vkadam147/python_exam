'''
    SET UPDATE METHODS:
    -------------------
    Update methods in set are used to perform mathematical operations
    BUT instead of returning a new set, they MODIFY the original set itself.

    IMPORTANT:
    ----------
    ✔ Original set gets changed
    ❌ No new set is returned (return value = None)

----------------------------------------------------------------------------------------------------

    1. intersection_update():
       ----------------------
       Syntax:
           A.intersection_update(B)

       Meaning:
           It keeps ONLY the common elements between set A and set B
           and removes all other elements from set A.

       Key Points:
           a. Modifies original set A
           b. Keeps common elements
           c. Faster than creating new set

       Example:
           A = {1, 2, 3, 4}
           B = {3, 4, 5, 6}

           A.intersection_update(B)
           print(A)

       Output:
           {3, 4}

----------------------------------------------------------------------------------------------------

    2. difference_update():
       --------------------
       Syntax:
           A.difference_update(B)

       Meaning:
           It removes all elements from set A that are also present in set B.
           After operation, only elements unique to A remain.

       Key Points:
           a. Modifies original set A
           b. Removes common elements
           c. Keeps only A - B

       Example:
           A = {1, 2, 3, 4}
           B = {3, 4, 5}

           A.difference_update(B)
           print(A)

       Output:
           {1, 2}

----------------------------------------------------------------------------------------------------

    3. symmetric_difference_update():
       --------------------------------
       Syntax:
           A.symmetric_difference_update(B)

       Meaning:
           It keeps elements which are NOT common between set A and set B.
           Common elements are removed from both sides.

       Formula:
           (A ∪ B) − (A ∩ B)

       Key Points:
           a. Modifies original set A
           b. Removes common elements
           c. Keeps non-common elements

       Example:
           A = {1, 2, 3, 4}
           B = {3, 4, 5, 6}

           A.symmetric_difference_update(B)
           print(A)

       Output:
           {1, 2, 5, 6}

----------------------------------------------------------------------------------------------------

    COMPARISON SUMMARY:
    -------------------

        Method                         Keeps                    Modifies Set
        --------------------------------------------------------------------
        intersection_update()          Common elements           Yes
        difference_update()            Elements only in A        Yes
        symmetric_difference_update()  Non-common elements       Yes

----------------------------------------------------------------------------------------------------

    MOST IMPORTANT EXAM RULE:
    -------------------------
        result = A.intersection_update(B)

        result -> None
        A      -> Updated set

----------------------------------------------------------------------------------------------------

    MEMORY TRICK:
    -------------
        intersection_update  -> keep same
        difference_update    -> remove same
        symmetric_difference -> remove same from both

----------------------------------------------------------------------------------------------------

'''
# intersction_update()
A={1,2,3,4}
B={2,3,4,5,6}
A.intersection_update(B)
print(f"Interscetion update:{A}")
print(B)

#differnce_update()
A={1,2,3,4}
B={2,3,4,5,6}
A.difference_update(B)
print(f"Difeerence updatte:{A}")
print(B)

#symmetric_difference_update()
A={1,2,3,4}
B={2,3,4,5,6}
A.symmetric_difference_update(B)
print(f"symmetric difference update:{A}")
print(B)


