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
data = pd.read_csv('BC_distances.csv')  # pandas library
cities = data.columns.tolist()
num_cities = len(cities)
adj_matrix = data.to_numpy()


def dijkstra(start):
    visited = [False] * num_cities
    distance = [math.inf] * num_cities
    distance[start] = 0

    for _ in range(num_cities):
        min_dist = math.inf
        min_index = -1

        for i in range(num_cities):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i

        visited[min_index] = True

        for i in range(num_cities):
            if not visited[i] and adj_matrix[min_index][i] > 0:
                if distance[i] > distance[min_index] + adj_matrix[min_index][i]:
                    distance[i] = distance[min_index] + adj_matrix[min_index][i]

    return distance


shortest_dist_results = {}
for i, city in enumerate(cities):
    shortest_distances = dijkstra(i)
    print(f"Shortest distances from {city}:")
    for j, dist in enumerate(shortest_distances):
        print(f"To {cities[j]}: {dist} km")
        shortest_dist_results[city] = shortest_distances
    print()

results_csv = pd.DataFrame(shortest_dist_results, index=cities)
results_csv.to_csv('BC_shortest_paths.csv', index=True)

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
