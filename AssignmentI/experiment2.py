import networkx as nx
import matplotlib.pyplot as plt
import statistics
import random
import Search_algorithms as sa

# random.seed(123)
# Here we add edge Weights
def edge_weight(graph,p):
    n=graph.number_of_nodes()
    max_weight=30
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                weight = random.randint(1, max_weight)
                graph.add_edge(i,j,weight=weight)

# draw the graph,and return a dictionary of node positions                 
def draw_graph(graph):
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw(graph, pos=pos, with_labels=True)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels,label_pos=0.8,font_size=5)

    plt.title(f'{graph}')
    # plt.show()
    return pos

# Add nodes with consistent positions 
def add_position(graph,n):
    grid_size = int(n ** 0.5)
    spacing = 1 / (grid_size + 1)
    positions = []
    for i in range(0, grid_size + 1): 
        for j in range(0, grid_size + 1):
            positions.append((i * spacing, j * spacing))         
    # Add n nodes with consistent positions
    for i in range(n):
        graph.add_node(i, pos=positions[i % len(positions)])



graph_1= nx.Graph()
graph_1.graph['p'] = 0.2
add_position(graph_1,10)
edge_weight(graph_1,0.2)
positions=draw_graph(graph_1)


graph_2= nx.Graph()
graph_2.graph['p'] = 0.4
add_position(graph_2,10)
edge_weight(graph_2,0.4)
positions=draw_graph(graph_2)

graph_3= nx.Graph()
graph_3.graph['p'] = 0.6
add_position(graph_3,10)
edge_weight(graph_3,0.6)
positions=draw_graph(graph_3)

graph_4= nx.Graph()
graph_4.graph['p'] = 0.8
add_position(graph_4,10)
edge_weight(graph_4,0.8)
positions=draw_graph(graph_4)




graph_5= nx.Graph()
graph_5.graph['p'] = 0.2
add_position(graph_5,20)
edge_weight(graph_5,0.2)
positions=draw_graph(graph_5)

graph_6= nx.Graph()
graph_6.graph['p'] = 0.4
add_position(graph_6,20)
edge_weight(graph_6,0.4)
positions=draw_graph(graph_6)

graph_7= nx.Graph()
graph_7.graph['p'] = 0.6
add_position(graph_7,20)
edge_weight(graph_7,0.6)
positions=draw_graph(graph_7)

graph_8= nx.Graph()
graph_8.graph['p'] = 0.8
add_position(graph_8,20)
edge_weight(graph_8,0.8)
positions=draw_graph(graph_8)





graph_9= nx.Graph()
graph_9.graph['p'] = 0.2
add_position(graph_9,30)
edge_weight(graph_9,0.2)
positions=draw_graph(graph_9)

graph_10= nx.Graph()
graph_10.graph['p'] = 0.4
add_position(graph_10,30)
edge_weight(graph_10,0.4)
positions=draw_graph(graph_10)

graph_11= nx.Graph()
graph_11.graph['p'] = 0.6
add_position(graph_11,30)
edge_weight(graph_11,0.6)
positions=draw_graph(graph_11)

graph_12= nx.Graph()
graph_12.graph['p'] = 0.8
add_position(graph_12,30)
edge_weight(graph_12,0.8)
positions=draw_graph(graph_12)



graph_13= nx.Graph()
graph_13.graph['p'] = 0.2
add_position(graph_13,40)
edge_weight(graph_13,0.2)
positions=draw_graph(graph_13)

graph_14= nx.Graph()
graph_14.graph['p'] = 0.4
add_position(graph_14,40)
edge_weight(graph_14,0.4)
positions=draw_graph(graph_14)

graph_15= nx.Graph()
graph_15.graph['p'] = 0.6
add_position(graph_15,40)
edge_weight(graph_15,0.6)
positions=draw_graph(graph_15)

graph_16= nx.Graph()
graph_16.graph['p'] = 0.8
add_position(graph_16,40)
edge_weight(graph_16,0.8)
positions=draw_graph(graph_16)




def random_path_finder(graph):
    adj_list={}
    non_island_nodes=set()
    fagaras=sa.Algorithms()

    for u, v, w in graph.edges(data=True):
        non_island_nodes.add(u)
        non_island_nodes.add(v)
        if u not in adj_list:
            adj_list[u] = []
        adj_list[u].append((v, w['weight']))
        if v not in adj_list:
            adj_list[v] = []
        adj_list[v].append((u, w['weight']))

    # Add island nodes to the adjacency list
    for node in graph.nodes():
        if node not in non_island_nodes:
            adj_list[node] = []

    # print(adj_list)

    nodes=list(graph.nodes())
    ten_nodes=random.sample(nodes, k=10)
    dfs_time=[]
    ucs_time=[]
    astar_time=[]
    dfs_path_length=[]
    ucs_path_length=[]
    astar_path_length=[]
    for i in range(len(ten_nodes)):
        for j in range(i+1,len(ten_nodes)):
            dfs_path=fagaras.average_calc(fagaras.dfs,adj_list,ten_nodes[i],ten_nodes[j],5)
            dfs_time.append(dfs_path[0])
            dfs_path_length.append(dfs_path[1])
            ucs_path=fagaras.average_calc(fagaras.ucs,adj_list,ten_nodes[i],ten_nodes[j],5)
            ucs_time.append(ucs_path[0])
            ucs_path_length.append(ucs_path[1])
            astar_path=fagaras.average_calc(fagaras.a_star,adj_list,ten_nodes[i],ten_nodes[j],5,positions)
            astar_time.append(astar_path[0])
            astar_path_length.append(astar_path[1])
    dfs_time=statistics.mean(dfs_time)
    ucs_time=statistics.mean(ucs_time)
    astar_time=statistics.mean(astar_time)
    dfs_path_length=statistics.mean(dfs_path_length)
    ucs_path_length=statistics.mean(ucs_path_length)
    astar_path_length=statistics.mean(astar_path_length)
    return (dfs_time,ucs_time,astar_time,dfs_path_length,ucs_path_length,astar_path_length)

def avg_time():
    graphs=[graph_1,graph_2,graph_3,graph_4,graph_5,graph_6,graph_7,graph_8,graph_9,graph_10,graph_11,graph_12,graph_13,graph_14,graph_15,graph_16]
    Average_time=[]
    for graph in graphs:
        dfs_time,ucs_time,astar_time,dfs_path,ucs_path,astar_path=random_path_finder(graph)
        Average_time.append((len(graph.nodes()),graph.graph['p'],dfs_time,ucs_time,astar_time,dfs_path,ucs_path,astar_path))
    return Average_time
def plot_time_graph():
    lst=avg_time()
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    nodes = [t[0] for t in lst]
    prob = [t[1]*50 for t in lst]
    dfs_time = [t[2] for t in lst]
    ucs_time = [t[3] for t in lst]
    astar_time = [t[4] for t in lst]
    dfs_path = [t[5] for t in lst]
    ucs_path = [t[6] for t in lst]
    astar_path = [t[7] for t in lst]

    ax.scatter(nodes,dfs_time,c='blue',s=prob,label='dfs time',alpha=0.5)
    ax.scatter(nodes,ucs_time,c='red',s=prob,label='ucs time',alpha=0.5)
    ax.scatter(nodes,ucs_time,c='green',s=prob,label='astar time',alpha=0.5)

    ax.set_xlabel('nodes')
    ax.set_ylabel('time')
    ax.set_title('time-node Plot')
    ax.legend()

    ax2.scatter(nodes,dfs_path,c='blue',s=prob,label='dfs path',alpha=0.5)
    ax2.scatter(nodes,ucs_path,c='red',s=prob,label='ucs path',alpha=0.5)
    ax2.scatter(nodes,astar_path,c='green',s=prob,label='astar path',alpha=0.5)

    ax2.set_xlabel('nodes')
    ax2.set_ylabel('path')
    ax2.set_title('path-node Plot')
    ax2.legend()
    
    plt.show()
plot_time_graph()