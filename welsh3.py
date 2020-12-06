""" Welsh Powell Implementation
Graph is dictionary with keys as vertex and values as vertices its connected to

"""

graph = {'A': ['C'], 'B': ['C', 'E'], 'C': ['A', 'B', 'D', 'E'], 'D': ['C'], 'E': ['B', 'C', 'F'], 'F': ['E', 'G'], 'G': ['F']}
#graph = {'A': ['B', 'C', 'D'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D'], 'D': ['A', 'B', 'C']} #K4 graph
# graph = {'A': ['B', 'C'],
# 'B': ['A', 'D', 'E'],
# 'C': ['A', 'E'],
# 'D': ['B', 'E', 'F'],
# 'E': ['B', 'C', 'D', 'F'],
# 'F': ['D', 'E']}
order = sorted(graph, key=lambda key: len(graph[key]), reverse=True) #order of vertices from max to min degree
colorings = {} #stores our final colorings
Color = 0

#didn't use adjacency matrix but may be helpful in future
#Following block from: https://stackoverflow.com/questions/37353759/how-do-i-generate-an-adjacency-matrix-of-a-graph-from-a-dictionary-in-python
# keys = sorted(graph.keys()) #sort nodes in alphabetical order
# size = len(keys)
# adj_matrix = [ [0]*size for i in range(size) ] #initialize adjacency adjcency matrix
# for a,b in [(keys.index(a), keys.index(b)) for a, row in graph.items() for b in row]:
#      adj_matrix[a][b] = 2 if (a==b) else 1

for vertex in order: #iterate through from max to min degree
    if vertex not in colorings: #skip if already colored
        colorings.update({vertex: Color}) #if not colored, assign color

        for nextVertex in order: #see if we can color any other vertex that color
            if nextVertex not in colorings: #skip if already colored
                isConnected = False #reset boolean

                #check if the vertex is connected to an already-colored graph of same color
                for alreadyColored in colorings:
                    for connectedIndex in range(len(graph[alreadyColored])):
                        #only care if its connected and the current color
                        if graph[alreadyColored][connectedIndex] == nextVertex and colorings[alreadyColored] == Color:
                            isConnected = True

                if not isConnected:
                    colorings.update({nextVertex: Color}) #color current color if not connected to anything this color
    Color += 1

print(colorings)
