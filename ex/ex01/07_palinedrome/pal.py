LETTERS='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
class Palindrome:

    @staticmethod
    def is_not_char(letter):
       return letter not in LETTERS

    @staticmethod
    def is_palindrome(text):
        i=0
        j=len(text)-1

        while (i<j):

            while Palindrome.is_not_char(text[i]):
                if (i>j): return False 
                i = i + 1 

            while Palindrome.is_not_char(text[j]):
                if (i>j): return Fasle 
                j = j - 1

            if text[i].upper() != text[j].upper():
               return False

            i = i + 1
            j = j - 1  

        return True
lines = ['Noel sees Leon.', 'hello']
print( [Palindrome.is_palindrome(x) for x in lines] )


'''
https://www.testdome.com/Questions/Python/Palindrome/4637

Question: Palindrome (Python)
Author: Anonymous
Skills: Python

Type: Public
 View score distribution

Expected time: 20min

Write a function that checks if a given sentence is a palindrome. A palindrome is a word, phrase, verse, or sentence that reads the same backward or forward. Only the order of English alphabet letters (A-Z and a-z) should be considered, other characters should be ignored.

For example, is_palindrome('Noel sees Leon.') should return true as spaces, period, and case should be ignored resulting with "noelseesleon" which is a palindrome since it reads same backward and forward.
'''
