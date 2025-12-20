'''
    set:
         1.An unordered collection of heterogeneous elements which is mutable and stored in single variable where duplicates are not allowed
----------------------------------------------------------------------------------------------------

         2.Key characterstics:
            a.unordered: Order is not preserved 
            b.Index based access is not possible
            c.mutable: set is mutable data structure where we can perform CRUD operation on set
            d.Heterogeneous: we can any type of data in set
            e.duplicates not allowed: In set data structure as name suggest it can store only unique elements and duplicate elements are removed from the set automatically
            f.set used hashtable to stpre data
            g.hashing method is used to get faster access in set
----------------------------------------------------------------------------------------------------

        3.set data structure is mainly used for performing mathematical operation on data
            1.union 
            2.intersection
            3.difference
            4.symmetric_difference
        4.we can perform set mathematical operation using operator as well as method given by set class
----------------------------------------------------------------------------------------------------

        5.operators:
            1.union (|)
            2.intersection(&)
            3.difference(-)
            4.symmetric_differenc(^)
            5.subset
                a.subset(<=)
                b.proper subset(<)
            6.superset(>=,>)
----------------------------------------------------------------------------------------------------

        6.using methods:
            let A={} and B={} are two sets
            1.A.union(B)-> It will return new set with combining all elements of set A and set B 
                A={1,2,3}
                B={1,4,5,6}
                A|B={1,2,3,4,5,6}
                A.union(B)={1,2,3,4,5,6}
----------------------------------------------------------------------------------------------------
           
             2.A.intersection(B): It will return common elements of set A and set B and return new set
                A={1,2,3}
                B={1,4,5,6,2}
                A&B={1,2}
                A.intersection(B)={1,2}
----------------------------------------------------------------------------------------------------

            3.A.difference(B): It will return new set containing elements which are not in B and which are not common in both A and B so just elements of A only
                A={1,2,3,4}
                B={2,3,5,6}
               A.difference(B)  OR (A-B)    ={1,4}
----------------------------------------------------------------------------------------------------

            4.B.difference(A):  It will return new set containing elements which are not in A and which are not common in both A and B so just elements of B only
                    A={1,2,3,4}
                    B={2,3,5,6}
                    B.difference(A) OR (B-A)={5,6}
----------------------------------------------------------------------------------------------------

            5.A.symmetric_difference(B): It will return new set containing elements of set A and set B which are not common
                        A={1,2,3,4}
                        B={2,3,5,6}
                        A.symmetric_differnec(B)  OR (A^B)  ->{1,4,5,6}
----------------------------------------------------------------------------------------------------
                    
'''
 
