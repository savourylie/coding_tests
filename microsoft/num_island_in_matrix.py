# Consider a matrix of 0s and 1s.
# If two 1s are adjacent to each other, they are considered connected.
# Find out the number of connected components there are in the matrix

def num_island_in_matrix(m):
	"""
	(2D-list) -> int
	"""
	num_row = len(m)
	num_col = len(m[0])

	island_list = []

	# Identify islands and put in a list
	for x in range(num_row):
		for y in range(num_col):
			if m[x][y] == 1:
				island_list.append([(x, y), None])

	# Assign parent index to each island, defaulting their own index
	# Create a matrix_to_list_map
	matrix_to_list_map = {}

	for i, x in enumerate(island_list):
		x[1] = i
		matrix_to_list_map[x[0]] = x[1]

	# Sanity check
	counter = 0
	for x in range(num_row):
		for y in range(num_col):
			if m[x][y] == 1:
				counter += 1

	assert counter == len(island_list)
	print("Sanity check passed.")

	visited_matrix = [[False] * num_col for _ in range(num_row)]

	for x in range(num_row):
		for y in range(num_col):
			visited_matrix[x][y] = True

			x_coords = [x, x - 1, x + 1]
			y_coords = [y, y - 1, y + 1]

			x_coords = [x for x in x_coords if num_row > x >= 0]
			y_coords = [y for y in y_coords if num_col > y >= 0]

			vicinity_coords = [(x, y) for x in x_coords for y in y_coords]
			vicinity_coords.remove((x, y))
			
			if m[x][y] == 1:
				for coord in vicinity_coords:
					if coord in matrix_to_list_map:
						own_index = matrix_to_list_map[(x, y)]
						near_index = matrix_to_list_map[coord]
						# print(island_list[matrix_to_list_map[(x, y)]])
						if m[coord[0]][coord[1]] and m[coord[0]][coord[1]] == 1:
							if visited_matrix[coord[0]][coord[1]] == False:
								island_list[near_index][1] = island_list[own_index][1]
								visited_matrix[coord[0]][coord[1]] = True
							else:
								island_list[own_index][1] = island_list[near_index][1]
								visited_matrix[coord[0]][coord[1]] = True

	print(island_list)
	
	for i, x in enumerate(island_list):
		while island_list[x[1]][1] != island_list.index(island_list[x[1]]):
			x[1] = island_list[x[1]][1]

	print(island_list)

	index_set = set([x[1] for x in island_list])

	return len(index_set)


def test_num_island_in_matrix():
	m1 = [[0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 0, 1]]
	m2 = [[1, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 0]]
	m3 = [[1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1]]
	m4 = [[1, 1, 0, 1, 0], [0, 0, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [1, 0, 1, 0, 0]]

	assert num_island_in_matrix(m1) == 2
	assert num_island_in_matrix(m2) == 3
	assert num_island_in_matrix(m3) == 3
	assert num_island_in_matrix(m4) == 6

	print("All tests passed.")

if __name__ == '__main__':
	test_num_island_in_matrix()