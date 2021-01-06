# Program will count Land which is close to each other

class Graph:

	def __init__(init, row, col, g):
		init.ROW = row
		init.COL = col
		init.graph = g
		#init row and col for graph

	def isSafe(init, i, j, visited):
		# check the function is available
		# row number is in range, column number
		# is in range and value is 1
		# and not yet visited
		return (i >= 0 and i < init.ROW and
				j >= 0 and j < init.COL and
				not visited[i][j] and init.graph[i][j])


	# A utility function to do DFS for a 2D
	# boolean matrix. It only considers
	# the 8 neighbours as adjacent vertices
	def DFS(init, i, j, visited):

		# These arrays are used to get row and
		# column numbers of 8 neighbours
		# of a given cell
		rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1];
		colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];

		# Mark this cell as visited
		visited[i][j] = True

		for k in range(8): # try to recursive in range
			if init.isSafe(i + rowNbr[k], j + colNbr[k], visited):
				init.DFS(i + rowNbr[k], j + colNbr[k], visited)

	# The main function that returns
	# count of islands in a given boolean
	# 2D matrix
	def countIslands(init):
		# Make a bool array to mark visited cells.
		# Initially all cells are unvisited
		visited = [[False for j in range(init.COL)]for i in range(init.ROW)]

		# Initialize count as 0 and travese
		# through the all cells of
		# given matrix
		count = 0
		for i in range(init.ROW):
			for j in range(init.COL):
				# If a cell with value 1 is not visited yet,
				# then new island found
				if visited[i][j] == False and init.graph[i][j] == 1:
					# Visit all cells in this island
					# and increment island count
					init.DFS(i, j, visited)
					count += 1

		return count
# start main function

graph = [[1, 1, 0, 0, 0],
		[0, 1, 0, 0, 1],
		[0, 0, 1, 1, 1],
		[0, 0, 0, 0, 0],
		[1, 0, 0, 0, 1]]


row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print ("Number of islands is:")
print (g.countIslands())
