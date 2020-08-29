"""
Finds anagram
"""


# Time complexity: O(nLog n)
# Space complexity: O(1)

def check_anagram(string1: str, string2: str):

    # if lengths are different then can not be anagram
    if len(string1) != len(string2):
        return False

    string1 = sorted(string1)
    string2 = sorted(string2)

    if string1 == string2:
        return True

    return False


# Time complexity: O(n), Space complexity: O(n)
def check_anagram2(string1: str, string2: str):
    count1 = {}
    count2 = {}

    if len(string1) != len(string2):
        return False

    for ch1 in string1:
        ascaii = ord(ch1)

        value = count1.get(ascaii, 0) + 1

        count1.update({ascaii: value})
    for ch2 in string2:
        ascaii = ord(ch2)
        value = count2.get(ascaii, 0) + 1
        count2.update({ascaii: value})

    for (c1, v1) in count1.items():
        v2 = count2.get(c1, -1)
        if v1 != v2:
            return False

    return True


if __name__ == '__main__':
    is_anagram = check_anagram2("abcd", "dabc")
    print(is_anagram)


