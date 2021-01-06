#Zombie Attack
def Zatt(graph):
	zombie = [] # set array for zombie position
	human = 0 # setting init human

	for i in range(len(graph)):
		for j in range(len(graph[0])):
			if(graph[i][j] == 2):
				zombie.append([i,j])
				# what if the graph's value is 2 then the zombie
			elif(graph[i][j] == 1):
				human = human + 1
				# what if the graph's value is 1 then the human
	if(human == 0):
		# case if there are not human
		return 0

	# setting before start Zombie attack
	day = 0 # day will be initially 0
	BFS = [ [1,0],
			[-1,0],
			[0,1],
			[0,-1] ]
	# this will be need for compare zombie and human's position
	# up down left right positon needed

	while(zombie):
		day = day + 1 # increase day
		# Using BFS method
		for i in range(len(zombie)):
			position = zombie.pop(0)
			# ex [0, 1]
				#[2, 0]
				#[2, 4]
			# find position of zombie
			for j in BFS:
				adj = [ position[0]+j[0] , position[1]+j[1] ]
				#find adjacent from zombie(around)
				if(adj[0]>=0 and adj[0]<len(graph) and adj[1]>=0 and adj[1]<len(graph[0])):
					# if there are human around zombie then human become zombie
					if(graph[adj[0]][adj[1]] == 1):
						graph[adj[0]][adj[1]] = 2
						human = human - 1
						# and human is gone by zombie (decreasing human)
						if(human == 0): # human all dead
							return day
						zombie.append(adj)
	return -1 #return -1 above all is not possible

m1 = [[1,2,1,0,0],[0,0,0,0,1],[2,0,0,0,2],[0,0,0,0,0]]
m2 = [[1,2,1,1,0],[0,0,0,0,1],[2,0,0,0,2],[0,0,0,1,1]]

print( Zatt(m1) )
print( Zatt(m2) )
