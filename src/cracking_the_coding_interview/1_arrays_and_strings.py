"""
Is Unique
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
def is_unique(string: str) -> bool:

    flag = [False] * 255
    print(flag)
    for c in string:
        print(c)
        val: int = ord(c)
        if flag[val]:
            return False
        flag[val] = True
    return True


"""
Check Permutation
Given two strings, write a method to decide if one is a permutation of the other
"""
def check_permutation(one: str, two: str) -> bool:

    if len(one) != len(two):
        return False

    one = [char.lower() for char in one]
    two = [char.lower() for char in two]
    one.sort()
    two.sort()

    for index in range(0, len(one)):
        if one[index] != two[index]:
            return False

    return True
