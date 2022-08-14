from graph.Graph import Graph
import sys
from collections import defaultdict


class Path(Graph):

    def __init__(self):
        super().__init__()
        self.possible_paths = []
        self.shortest_path = []
        self.weight = defaultdict()

    def addWeightedEdge(self, u, v, w):
        self.graph[u].append(v)
        self.weight[(u, v)] = w

    # print all the possible path between two nodes
    def allPossiblePath(self, source, destination, visited, path):
        visited[source] = True
        # this will work in case of all the nodes are continuous numbers or use a dict

        path.append(source)
        if source == destination:
            print(path)
        else:
            for node in self.graph[source]:
                if not visited[node]:
                    visited[node] = True
                    self.allPossiblePath(node, destination, visited, path)

        path.pop()
        visited[source] = False

    def AllPathsUtil(self, s, d):
        visited = [False] * len(self.getAllVertices())
        self.allPossiblePath(s, d, visited, [])

    # print the path which costs us less, also the cost weighted graph
    # using dijkstra algorithm
    def shortestPath(self, source, destination):
        # set the distance from source vertex, if direct edge is there set the weight otherwise set infinity
        # assuming all the nodes are indexed basis eg: 0,1,2,3,4,5 so on

        distance = [sys.maxsize] * len(self.getAllVertices())
        distance[source] = 0
        # update the distance if current node's distance is larger than previous nodes distance + current edge weight
        # for node in self.graph[source]:
        #     distance[node] = self.weight[(source, node)]

        # apply bfs and keep updating and repeat the above steps to update distance for each node

        visited = [False] * len(self.graph)
        queue = [source]
        visited[source] = True
        # this will work in case of all the nodes are continuous numbers or use a dict
        while queue:
            # pop the queue and put all the adjacent nodes inside queue
            source = queue.pop(0)
            self.visited_nodes.append(source)
            for node in self.graph[source]:
                # print(self.weight[(source, node)])
                if distance[node] > self.weight[(source, node)] + distance[source]:
                    distance[node] = self.weight[(source, node)] + distance[source]
                    # marking this node as false in case of distance update so that this node gets considered again
                    visited[node] = False
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

        return distance


p = Path()
p.addWeightedEdge(0, 1, 2)
p.addWeightedEdge(0, 2, 4)
p.addWeightedEdge(1, 4, 1)
p.addWeightedEdge(1, 2, 1)
p.addWeightedEdge(1, 3, 7)
p.addWeightedEdge(2, 4, 3)
p.addWeightedEdge(4, 3, 2)
p.addWeightedEdge(4, 5, 5)
p.addWeightedEdge(3, 5, 1)
p.addVertices(5)

print(p.shortestPath(0, 5))
