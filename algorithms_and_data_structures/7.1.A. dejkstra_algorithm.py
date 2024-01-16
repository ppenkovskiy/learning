graph = {}

graph['start'] = {}
graph['start']['a'] = 2
graph['start']['b'] = 5

graph['a'] = {}
graph['a']['b'] = 8
graph['a']['d'] = 7

graph['b'] = {}
graph['b']['c'] = 4
graph['b']['d'] = 2

graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3

graph['d'] = {}
graph['d']['fin'] = 1

graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 2
costs['b'] = 5
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
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
