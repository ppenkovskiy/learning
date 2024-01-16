graph = {}

graph['start'] = {}
graph['start']['a'] = 10

graph['a'] = {}
graph['a']['c'] = 20

graph['b'] = {}
graph['b']['a'] = 1
graph['b']['c'] = 1

graph['c'] = {}
graph['c']['fin'] = 30

graph['fin'] = {}

costs = {}
costs['a'] = 10
costs['b'] = float('inf')
costs['c'] = float('inf')
costs['fin'] = float('inf')

parents = {}
parents['a'] = 'start'
parents['b'] = None
parents['c'] = None
parents['fin'] = None

processed_nodes = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed_nodes:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed_nodes.append(node)
    node = find_lowest_cost_node(costs)

print(costs['fin'])
