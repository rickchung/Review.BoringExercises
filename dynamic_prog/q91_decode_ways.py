"""https://leetcode.com/problems/decode-ways/
"""

# %%

test_cases = [
    ("12", 2),
    ("226", 3),
    ("02", 0),
    ("0", 0),
    ("10", 1),
    ("100", 0),
    ("2611055971756562", 4),
    ("2101", 1),
    ("012", 0),
    ("12120", 3),
]


def num_decoding(s: str) -> int:

    lookup = {str(i) for i in range(1, 27)}
    def is_valid(a): return a in lookup

    if len(s) == 1:
        return 1 if is_valid(s[0]) else 0

    if s[0] == '0':
        return 0

    _s = []
    i = 0
    while i < len(s):
        if s[i] == '0':
            if is_valid(s[i-1] + s[i]):
                _s.pop()
                _s.append(s[i-1] + s[i])
                i += 1
            else:
                print(s[i-1] + s[i], "is invalid. Preprocess Abort")
                return 0
        else:
            _s.append(s[i])
            i += 1

    print("Input", s, _s)
    s = _s

    n_ways = [0] * len(s)
    n_ways[0] = 1 if is_valid(s[0]) else 0
    for i in range(1, len(s)):
        if n_ways[i-1] == 0:
            continue

        # print("Adding", s[i])
        # If the current value to add is valid
        if is_valid(s[i]):
            # If the (i-1, i) is also valid
            if is_valid(s[i-1] + s[i]):
                # When the seq goes beyond 3 items
                if i >= 3:
                    n_ways[i] = n_ways[i-1] + n_ways[i-2]
                else:
                    n_ways[i] = n_ways[i-1] + 1
                # print(s[i-1] + s[i], "is valid. Increase.", n_ways[i])

            # Otherwise, the value won't change
            else:
                n_ways[i] = n_ways[i-1]
                # print(s[i-1] + s[i], "is not valid. Stay.", n_ways[i])

        # If the current value to add is not valid (it's 0)
        else:
            # A zero can only be handled as (i-1, i)
            if is_valid(s[i-1] + s[i]):
                # print(s[i-1] + s[i], "is valid. Merge")
                n_ways[i] = max(n_ways[i-1] - n_ways[i-2] + 1, 1)
            # If a zero cannot be handled, the decoding fails
            else:
                # print(s[i-1] + s[i], "is not valid. Abort")
                return 0

    print("Output", n_ways)
    return n_ways[-1]


for t, a in test_cases:
    rt = num_decoding(t)
    print()
    if not rt == a:
        raise Exception("Failed")
