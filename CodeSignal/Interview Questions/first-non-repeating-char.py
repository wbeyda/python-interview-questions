"""
Author: Warren Beyda 2020
program to find first repeating character in a given string
program runs at O(n^2)
converted from Java example found on
https://www.youtube.com/watch?v=5co5Gvp_-S0
"""

def first_non_repeating_char(str):
    hashmap = {}
    for i in range(len(str)):
        if str[i] not in hashmap:
            hashmap[str[i]] = 1
        else:
            hashmap[str[i]] += 1

    for i in hashmap:
        if hashmap[i] == 1:
            return i

    return None

if __name__ == '__main__':
    print(first_non_repeating_char("aaabcc"))
    print(first_non_repeating_char("abcbad"))
    print(first_non_repeating_char("abcabcabc"))

