graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# print(type(graph['start']))
# print(graph['start'].keys())
# print(graph['start']['a'])
# print(graph['start']['b'])

graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {} # end node has no neighbors

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed_nodes = []


