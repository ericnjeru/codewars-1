# Description:
# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(string):
    if not string:
        return ''
    if len(string) == 1:
        return string
    for s in string:
        new_string = string.lower()
        count = new_string.count(s.lower())
        if count == 1:
            return (s)
    return ''



# Tests
Test.describe('Basic Tests')
Test.it('should handle simple tests')
Test.assert_equals(first_non_repeating_letter('a'), 'a')
Test.assert_equals(first_non_repeating_letter('stress'), 't')
Test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

Test.it('should handle empty strings')
Test.assert_equals(first_non_repeating_letter(''), '')

Test.it('should handle all repeating strings')
Test.assert_equals(first_non_repeating_letter('abba'), '')
Test.assert_equals(first_non_repeating_letter('aa'), '')

Test.it('should handle odd characters')
Test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
Test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')

Test.it('should handle letter cases')
Test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
Test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')

Test.describe('Random Tests')
from random import randint
sol=lambda s: (lambda uniq: ([a for a in s if s.lower().count(a.lower())==1] or [""])[0])(set(s.lower()))
base="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789;,:."

for _ in range(40):
    s="".join([base[randint(0,len(base)-1)] for q in range(randint(10,60))])
    Test.it ("Should work for "+repr(s))
    Test.assert_equals(first_non_repeating_letter(s),sol(s),"It should work for random inputs too")