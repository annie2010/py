class AreAnagrams:

    @staticmethod
    def are_anagrams(a, b):
        lookup = {} ## {l1:c1, l2:c2, l3:c3, ..}

        for x in a:
            if x in lookup:
                lookup[x] = lookup[x] +1
            else:
                lookup[x] = 1

        for y in b:
            if y not in lookup:
                return False
            else:
                if lookup[y] == 0:
                    return False
                else:  
                    lookup[y] = lookup[y] - 1 

        return True

pairs = [['neural', 'unreal'], ['hello', 'world']]
print( [ AreAnagrams.are_anagrams(x[0], x[1]) for x in pairs ] )

'''
Question: AreAnagrams (Python)
Author: Anonymous
Skills: Python

Type: Public
 View score distribution

Expected time: 15min

An anagram is a word formed from another by rearranging its letters, using all the original letters exactly once; for example, orchestra can be rearranged into carthorse.

Write a function that checks if two words are anagrams of each other.

For example, are_anagrams('neural', 'unreal') should return true as arguments are anagrams of each other.


https://www.testdome.com/Questions/Python/AreAnagrams/4639
'''
