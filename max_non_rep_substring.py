"""
Non rep substring
"""


def longest_substring(string: str):
    my_set = set()

    # Pointers
    i = j = 0
    max_count = 0

    while i < len(string) and j < len(string):
        # if not in set add it and increment j
        if not string[j] in my_set:
            my_set.add(string[j])
            j += 1
            max_count = max(max_count, j-i)

        else:
            # if it is on set remove its previous occurrence. inc i
            my_set.remove(string[i])
            i += 1

    return max_count


if __name__ == '__main__':
    print(longest_substring("abbcded"))
