"""
Implementation of shortest path algorithms Dijkstara in chicago sketch road network
"""
def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information. It will give the adjacency list of the given graph since the 
        no. of edges are relatively low and hence we do not want to use large storage by creating 933*933 matrix where as
        there are only 2950 edges
    """
    graph_object = {}
    # Change network name and ensure that tntp file exists in the same working directory
    network_name = "ChicagoSketch_net.tntp"
    try:
        with open(network_name, 'r') as f:
            lines = f.readlines()
            for line in lines[9:]:
                data = line.split('\t')
                graph_object.setdefault(int(data[1]), []).append((int(data[2]),float(data[5])))
        return graph_object
    except Exception as e:
        print('Error in creating graph object', e)
        return graph_object

"""Implementation using adjacency list"""

def closest_vertex(dist, visited , graph_object):
    min_d = float('inf')

    for v in graph_object:
        if v not in visited and dist[v] < min_d:
            min_d = dist[v]
            min_vertex = v
    return min_vertex

def dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        dist = {s: float('inf') for s in graph_object}
        visited = set()
        dist[source] = 0

        for nd in graph_object.keys():
            u = closest_vertex(dist, visited, graph_object)
            visited.add(u)
            if destination in visited:
                shortest_path_distance= dist[destination]
                break

            for node, weight in graph_object[u]:
                if node not in visited and dist[node] > dist[u] + weight:
                    dist[node] = dist[u] + weight
        return shortest_path_distance
    except:
        return shortest_path_distance

# """Implementation using heap (faster) using builtin heapq module"""

# import heapq as hq
# def dijkstra(source: int, destination: int, graph_object) -> int:
#     """
#     Dijkstra's algorithm.

#     Args:
#         source (int): Source stop id
#         destination (int): : destination stop id
#         graph_object: python object containing network information

#     Returns:
#         shortest_path_distance (int): length of the shortest path.

#     Warnings:
#         If the destination is not reachable, function returns -1
#     """
#     shortest_path_distance = -1
#     try:
#         heap = [(0, source)]
#         distance_dict = {}

#         while heap:
#             dist, node = hq.heappop(heap)
#             #If we have the destination node in distance then we already know the shortest distance between source & dest. node
#             if destination in distance_dict:
#                 break
#             # will contain the nodes which were encounteres earlier
#             if node in distance_dict:
#                 continue  
            
#             #New node and hence we add it in the distances dictionary
#             distance_dict[node] = dist
#             for neighbor, weight in graph_object[node]:
#                 if neighbor not in distance_dict:
#                     hq.heappush(heap, (dist + weight, neighbor))
#         shortest_path_distance = distance_dict[destination]
        
#         return shortest_path_distance
#     except:
#         return shortest_path_distance