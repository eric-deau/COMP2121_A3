import pandas as pd
import math

# 1.
def fourBitPalindrome(bitNum):
    count = 0
    current_state = 'start'
    states = {
        'start': {'0': 's0', '1': 's1'},
        's0': {'0': 's00', '1': 's01'},
        's1': {'0': 's10', '1': 's11'},
        's10': {'0': 's100', '1': 's01'},
        's00': {'0': 's000', '1': 's10'},
        's01': {'0': 's10', '1': 's011'},
        's11': {'0': 's10', '1': 's111'},
        's011': {'0': 's0110', '1': 's111'},
        's100': {'0': 's000', '1': 's1001'},
        's111': {'0': 's10', '1': 's1111'},
        's000': {'0': 's0000', '1': 's01'},
        's0000': {'0': 's0000', '1': 's01'},
        's1111': {'0': 's10', '1': 's1111'},
        's1001': {'0': 's10', '1': 's011'},
        's0110': {'0': 's100', '1': 's01'}
    }
    accepting_states = {'s0110', 's0000', 's1001', 's1111'}

    for char in bitNum:
        if char != '0' and char != '1':
            continue
        if current_state in states and char in states[current_state]:
            current_state = states[current_state][char]
            if current_state in accepting_states:
                count += 1

    return count


print(fourBitPalindrome("011001011100"))

eBinary = open("BINARY_DIGITS_OF_E.txt", "r")
print(fourBitPalindrome(eBinary.read()))

# 6.


# 7.
# initializing string
test_str = "I WOULD NOT EAT THEM HERE OR THERE. I WOULD NOT EAT THEM ANYWHERE."

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# Sorting the hashmap by value in descending order
sorted_freq = {k: v for k, v in sorted(all_freq.items(), key=lambda item: item[1], reverse=True)}

# Printing the sorted result
print("Characters sorted by their counts:\n" + str(sorted_freq))