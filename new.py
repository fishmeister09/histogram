def find_paths(matrix, start_pos, k):
    rows = len(matrix)
    cols = len(matrix[0])
    memo = [[[None] * (k + 1) for _ in range(cols)] for _ in range(rows)]
    

    def get_paths(row, col, time):
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return []
        if time > k:
            return []
        if time >= k:
            return [[[row, col, time]]]  
        if memo[row][col][time] is not None:
            return memo[row][col][time]

        possible_paths = []
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row = row + dr
            new_col = col + dc
            paths = get_paths(new_row, new_col, time + 1)
            for path in paths:
                possible_paths.append([[row, col, time]] + path)

        memo[row][col][time] = possible_paths
        return possible_paths

    return get_paths(start_pos[0], start_pos[1], 0)


#function to generate mxn matrix
def generate_matrix(m,n):
    matrix = [[0 for x in range(m)] for y in range(n)]
    return matrix

matrix = generate_matrix(3,3)


start_position = (0, 0)
treasure_position = (2,2)
path_length = 8

paths = find_paths(matrix, start_position, path_length)

# Printing the paths
combined_path=[]

paths_after_filtering=0
print(paths)

for path in paths:
    if (
        path[-1][0] == treasure_position[0]
        and path[-1][1] == treasure_position[1]
        and (
            (path_length % 2 == 0 and path[-1][2] == path_length)  # for even path_length
            or (path_length % 2 == 1 and path[-1][2] == path_length - 1)  # for odd path_length
        )
    ):
        paths_after_filtering += 1
        combined_path.extend(path)


print(paths_after_filtering)
print(len(paths))


import matplotlib.pyplot as plt
from collections import defaultdict

frequency = defaultdict(int)

for item in combined_path:
    i = tuple(item)
    frequency[i] += 1

position, freqs = zip(*frequency.items())

plt.bar(range(len(position)), freqs)
plt.xticks(range(len(position)), position)

plt.xlabel('Position')
plt.ylabel('Frequency')
plt.title('Frequency vs. Position')

plt.show()
