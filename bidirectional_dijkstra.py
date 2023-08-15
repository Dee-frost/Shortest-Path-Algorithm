"""
Implementation of shortest path algorithms Bi-directional Dijkstara in chicago sketch road network
"""
def reverse_graph(graph_object):
    """
    Gives reverse graph in adjacency list format to allow for backward search from destination node
    
    Args: 
        Graph object: original graph object in adjacency list format
    
    Returns:
        Graph object which is reverse of the original network
    """
    reversed_graph = {}
    for i in graph_object.keys():
        for j in graph_object[i]:
            reversed_graph.setdefault(j[0], []).append((i,j[1]))
    return reversed_graph

def closest_vertex(dist, visited , graph_object):
    min_d = float('inf')

    for v in graph_object:
        if v not in visited and dist[v] < min_d:
            min_d = dist[v]
            min_vertex = v
    return min_vertex

def bidirectional_dij(source: int, destination: int, graph_object) -> int:
    """
    Bi-directional Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    reversed_graph = reverse_graph(graph_object)
# The idea is to traverse from the source node and simultaneously traverse backward from destination node. If we
# found a shortest path from source node to intermediate node and we also found out the shortest path in reversed
# graph from destination node to the same intermediate node then sum of these two distances will give the shortest
# path between source node and destination node, and hence that was our terminating condition that the searched from
# both the direction find some intermediate node.

# Then we need to ensure that the next node is same in both direction which will then establish that intersection node is
# indeed present in the shortest path between source and destination
    shortest_path_distance = -1
    try:
        dist_f = {s: float('inf') for s in graph_object}
        dist_b = {s: float('inf') for s in graph_object}
        visited_f = set()
        visited_b = set()
        dist_f[source] = 0
        dist_b[destination] = 0

        for _ in graph_object.keys():
            u_f = closest_vertex(dist_f, visited_f, graph_object)
            u_b = closest_vertex(dist_b, visited_b, reversed_graph)
            visited_f.add(u_f)
            visited_b.add(u_b)
                
            for node1, weight1 in graph_object[u_f]:
#                 print("=====================================================")
#                 print(node1,weight1)
#                 print(dist_f[node1], dist_f[u_f] + weight1)
                if node1 not in visited_f and dist_f[node1] > dist_f[u_f] + weight1:
                    dist_f[node1] = dist_f[u_f] + weight1
#                     print("changing for node:",node1)
#                 print(dist_f[node1])
                    
            for node, weight in reversed_graph[u_b]:
                if node not in visited_b and dist_b[node] > dist_b[u_b] + weight:
                    dist_b[node] = dist_b[u_b] + weight
                    
            if  len(visited_f.intersection(visited_b))>1 :
#                 print("common nodes:", list(visited_f.intersection(visited_b)))
                next_u_f = closest_vertex(dist_f, visited_f, graph_object)
                next_u_b = closest_vertex(dist_b, visited_b, reversed_graph)
                common_node_found = list(visited_f.intersection(visited_b))
                dist = float('inf')

                if ((next_u_f in visited_b) and (next_u_b in visited_f)):
                    for common_nodes in common_node_found:
                        if dist > dist_f[common_nodes]+dist_b[common_nodes]:
                            dist = dist_f[common_nodes]+dist_b[common_nodes]
                    shortest_path_distance=dist
                    break
                    
        return shortest_path_distance
    except:
        return shortest_path_distance