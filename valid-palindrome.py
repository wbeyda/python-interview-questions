"""
solution for a leetcode problem
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/883/
"""
import re

def isPalindrome(s):
    stripped_string = re.sub(r'\W+|_', '', s).lower()
    if stripped_string[::-1] == stripped_string:
        return True
    else:
        return False


if __name__ == '__main__':
    test_string_1 = "A man, a plan, a canal: Panama"
    test_string_2 = "Race a Car"
    test_string_3 = "racecar"
    test_string_4 = "ab_a"
    print(isPalindrome(test_string_1)) #True
    print(isPalindrome(test_string_2)) #False
    print(isPalindrome(test_string_3)) #True
    print(isPalindrome(test_string_4)) #True
