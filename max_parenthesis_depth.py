"""
Find max parenthesis depth
"""


def find_max_depth(string: str):
    current_max = 0     # Current Max
    max_depth = 0       # Final max track

    for i in range(len(string)):
        if string[i] == '(':
            current_max += 1
            if current_max > max_depth:
                max_depth = current_max

        elif string[i] == ')':
            if current_max > 0:
                current_max -= 1
            else:
                return -1

    # Final sanity check that if, string is balanced or not.
    if current_max != 0:
        return -1

    return max_depth


if __name__ == "__main__":
    expr = "( ((X)) (((Y))) )"
    print(find_max_depth(expr))
