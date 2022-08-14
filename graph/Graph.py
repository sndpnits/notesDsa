from collections import defaultdict


# representing graph with a simple dictionary to keep track of all edges and vertices
# default dict avoids the keyError while adding edges to a new vertices
# we can start with any of the nodes as source and with visited_nodes it can display the path it went through
# this way we will be able to know if we reach from one source node to any destination node by just checking
# if destination node exists in visited_nodes
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_nodes = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # this method will be used when there is no path to any other node(uni directional graph)
    def addVertices(self, v):
        self.graph[v] = []

    def getAllVertices(self):
        return self.graph.keys()

    # get all the edges, iterate through all the all the vertices and iterate again through the node it is connected to
    def getAllEdges(self):
        edges = []
        for vertices in self.graph:
            for edge in self.graph[vertices]:
                edges.append((vertices, edge))

        return edges

    def BFS(self, source):
        # created a visited array to keep track of node visit
        visited = [False] * len(self.graph)

        queue = [source]
        visited[source] = True
        # this will work in case of all the nodes are continuous numbers or use a dict
        while queue:
            # pop the queue and put all the adjacent nodes inside queue
            popped = queue.pop(0)
            self.visited_nodes.append(popped)
            for node in self.graph[popped]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

    def DFS(self, source):
        # created a visited array to keep track of node visit
        visited = [False] * len(self.graph)
        # print(visited)

        stack = [source]
        visited[source] = True
        # this will work in case of all the nodes are continuous numbers or use a dict
        while stack:
            # pop the queue and put all the adjacent nodes inside queue
            popped = stack.pop(-1)
            self.visited_nodes.append(popped)
            for node in self.graph[popped]:
                if not visited[node]:
                    stack.append(node)
                    visited[node] = True


class Path(Graph):
    # print all the possible path between two nodes
    def allPossiblePath(self, source, destination):
        pass

    # print the path which costs us less, also the cost weighted graph
    def shortestPath(self, source, destination):
        pass

g = Path()
#
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)
# g.addEdge(1, 4)
# g.addEdge(2, 5)
# g.addEdge(3, 6)
# g.addVertices(4)
# g.addVertices(5)
# g.addVertices(6)

# g.BFS(2)
# print("BFS", g.visited_nodes)

# g.BFS(0)
# print("DFS", g.visited_nodes)

