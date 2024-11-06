#BellmanFord single source shortest path

#Problem: find the shortest path to every other node from a source node
#Input: dictionary of directional edges, and their corresponding weights
#edge[(u,v)] = weight from u to v
#Return a dictionary with all nodes, and their corresponding shortest path

#will error if your edges create a cycle with a combined a weight that is negative

#Time complexity: O(n * m)
#loop through all edges n-1 times


def bellman_ford_single_source_shortest_path(edges:dict, source:int) -> dict:
    class Node():
        def __init__(self, num, weight = None):
            self.num = num
            self.weight = weight
            self.path = []
        def __str__(self):
            w = self.weight if self.weight!=None else "Infinity"
            return f"Node: {self.num}: Weight = {w}, Path = {self.path}"
    nodes = {}
    nodes[source] = Node(source, 0)
    nodes[source].path = [source]
    for edge in edges.keys(): #create node O(e)
        nodes[edge[0]] = nodes.get(edge[0], Node(edge[0]))
        nodes[edge[1]] = nodes.get(edge[1], Node(edge[1]))
    for n in range(len(edges.items())-1): #relaxation loop through all edges n-1 times --> O(n)
        changed = False
        for edge, weight in edges.items():
            u = nodes[edge[0]].weight
            v = nodes[edge[1]].weight
            if u != None:
                new_weight = u + weight
                if v is None or v > new_weight:
                    nodes[edge[1]].weight = new_weight
                    nodes[edge[1]].path = nodes[edge[0]].path.copy() + [nodes[edge[1]].num]
                    changed = True
        if not changed: break #if no weights are changed then it is stable and you can stop


    return nodes

if __name__ == '__main__':
    edges = {(1,2):6,(1,3):5,(1,4):5,(2,5):-1,(3,5):1,(3,2):-2,(4,6):-1,(4,3):-2,(5,7):3,(6,7):3}
    source = 6
    nodes = bellman_ford_single_source_shortest_path(edges, source)

    for node in nodes.values():print(node)


