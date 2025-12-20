'''
    SET RELATIONSHIP & COMPARISON METHODS:
    -------------------------------------
    These methods are used to check the relationship between two sets.
    They return Boolean values (True / False).

    IMPORTANT:
    ----------
    ✔ These methods DO NOT modify the set
    ✔ They are mainly used for comparison and validation

----------------------------------------------------------------------------------------------------

    1. issubset():
       -------------
       Syntax:
           A.issubset(B)

       Meaning:
           Checks whether ALL elements of set A are present in set B.

       Mathematical meaning:
           A ⊆ B

       Example:
           A = {1, 2}
           B = {1, 2, 3, 4}

           print(A.issubset(B))

       Output:
           True

       Explanation:
           Every element of A exists in B

----------------------------------------------------------------------------------------------------

    2. issuperset():
       ---------------
       Syntax:
           A.issuperset(B)

       Meaning:
           Checks whether set A contains ALL elements of set B.

       Mathematical meaning:
           A ⊇ B

       Example:
           A = {1, 2, 3, 4}
           B = {2, 3}

           print(A.issuperset(B))

       Output:
           True

       Explanation:
           All elements of B are present in A

----------------------------------------------------------------------------------------------------

    3. isdisjoint():
       ---------------
       Syntax:
           A.isdisjoint(B)

       Meaning:
           Checks whether two sets have NO common elements.

       Mathematical meaning:
           A ∩ B = Ø

       Example:
           A = {1, 2, 3}
           B = {4, 5, 6}

           print(A.isdisjoint(B))

       Output:
           True

       Explanation:
           There are no common elements between A and B

----------------------------------------------------------------------------------------------------

    4. SUBSET using OPERATORS:
       ------------------------
       a. Subset (<=)
           Syntax:
               A <= B
           Meaning:
               A is subset of B (may be equal)

       b. Proper Subset (<)
           Syntax:
               A < B
           Meaning:
               A is subset of B but NOT equal

       Example:
           A = {1, 2}
           B = {1, 2, 3}

           print(A <= B)   # True
           print(A < B)    # True

----------------------------------------------------------------------------------------------------

    5. SUPERSET using OPERATORS:
       --------------------------
       a. Superset (>=)
           Syntax:
               A >= B
           Meaning:
               A is superset of B (may be equal)

       b. Proper Superset (>)
           Syntax:
               A > B
           Meaning:
               A is superset of B but NOT equal

       Example:
           A = {1, 2, 3}
           B = {1, 2}

           print(A >= B)   # True
           print(A > B)    # True

----------------------------------------------------------------------------------------------------

    COMPARISON SUMMARY TABLE:
    -------------------------

        Method / Operator    Purpose
        ----------------------------------------------
        issubset()           Check if A ⊆ B
        issuperset()         Check if A ⊇ B
        isdisjoint()         Check no common elements
        <=                   Subset (may be equal)
        <                    Proper subset
        >=                   Superset (may be equal)
        >                    Proper superset

----------------------------------------------------------------------------------------------------

    EXAM IMPORTANT POINTS:
    ----------------------
    ✔ issubset(), issuperset(), isdisjoint() return Boolean
    ✔ These methods DO NOT modify sets
    ✔ Used mainly in validation logic

----------------------------------------------------------------------------------------------------

    ONE-LINE EXAM ANSWER:
    ---------------------
    Set relationship methods are used to compare two sets and check subset,
    superset or disjoint relationships between them.

----------------------------------------------------------------------------------------------------
'''
# 1.A.issubset(B)
A={1,2,3}
B={1,2,3,4}
print(f"A.issubset(B):{A.issubset(B)}")# True
print(f"B.issubset(A):-{B.issubset(A)}") #False


#2.A.issuperset(B)
A={1,2,3,4,5}
B={1,2,3}
print(f"A.issuperset(B):{A.issuperset(B)}")
print(f"B.issuperset(A):{B.issuperset(A)}")


#3.A.isdisjoint(B)
A={1,2,3}
B={5,6,7}
print(f"A.isdisjoint(B):{A.isdisjoint(B)}")