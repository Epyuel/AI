import networkx as nx
import matplotlib.pyplot as plt
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
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels,label_pos=0.8,font_size=8)

    plt.title(f'{graph}')
    plt.show()
    return pos

# Add nodes with consistent positions 
def add_position(graph):
    n=10
    grid_size = int(n ** 0.5)
    spacing = 1 / (grid_size + 1)
    positions = []
    for i in range(0, grid_size + 1): 
        for j in range(0, grid_size + 1):
            positions.append((i * spacing, j * spacing))         
    # Add n nodes with consistent positions
    for i in range(n):
        graph.add_node(i, pos=positions[i % len(positions)])


algorithms=sa.Algorithms()
graph_1= nx.Graph()
add_position(graph_1)
edge_weight(graph_1,0.2)
positions=draw_graph(graph_1)


# graph_2= nx.erdos_renyi_graph(10, 0.4)
# add_position(graph_2)
# edge_weight(graph_2)
# draw_graph(graph_2)

# graph_3= nx.erdos_renyi_graph(10, 0.6)
# add_position(graph_3)
# edge_weight(graph_3)
# draw_graph(graph_3)

# graph_4= nx.erdos_renyi_graph(10, 0.8)
# add_position(graph_4)
# edge_weight(graph_4)
# draw_graph(graph_4)




# graph_5= nx.erdos_renyi_graph(20, 0.2)
# add_position(graph_5)
# edge_weight(graph_5)
# draw_graph(graph_5)

# graph_6= nx.erdos_renyi_graph(20, 0.4)
# add_position(graph_6)
# edge_weight(graph_6)
# draw_graph(graph_6)

# graph_7= nx.erdos_renyi_graph(20, 0.6)
# add_position(graph_7)
# edge_weight(graph_7)
# draw_graph(graph_7)

# graph_8= nx.erdos_renyi_graph(20, 0.8)
# add_position(graph_8)
# edge_weight(graph_8)
# draw_graph(graph_8)






# #30 nodes

# graph_9= nx.erdos_renyi_graph(30, 0.2)
# add_position(graph_9)
# edge_weight(graph_9)
# draw_graph(graph_9)

# graph_10= nx.erdos_renyi_graph(30, 0.4)
# add_position(graph_10)
# edge_weight(graph_10)
# draw_graph(graph_10)
# graph_11= nx.erdos_renyi_graph(30, 0.6)
# add_position(graph_11)
# edge_weight(graph_11)
# draw_graph(graph_11)

# graph_12= nx.erdos_renyi_graph(30, 0.8)
# add_position(graph_12)
# edge_weight(graph_12)
# draw_graph(graph_12)



# #40 nodes

# graph_13= nx.erdos_renyi_graph(40, 0.2)
# add_position(graph_13)
# edge_weight(graph_13)
# draw_graph(graph_13)

# graph_14= nx.erdos_renyi_graph(40, 0.4)
# add_position(graph_14)
# edge_weight(graph_14)
# draw_graph(graph_14)

# graph_15= nx.erdos_renyi_graph(40, 0.6)
# add_position(graph_15)
# edge_weight(graph_15)
# draw_graph(graph_15)

# graph_16= nx.erdos_renyi_graph(40, 0.8)
# add_position(graph_16)
# pos_dict=nx.get_node_attributes(graph_16,'pos')
# print(pos_dict)
# edge_weight(graph_16)
# draw_graph(graph_16)





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
    for i in range(len(ten_nodes)):
        for j in range(i+1,len(ten_nodes)):
            dfs_path=fagaras.average_calc(fagaras.dfs,adj_list,ten_nodes[i],ten_nodes[j],10000)
            dfs_time.append((ten_nodes[i],ten_nodes[j],dfs_path[0]))
            ucs_path=fagaras.average_calc(fagaras.ucs,adj_list,ten_nodes[i],ten_nodes[j],10000)
            ucs_time.append((ten_nodes[i],ten_nodes[j],ucs_path[0]))
            astar_path=fagaras.average_calc(fagaras.a_star,adj_list,ten_nodes[i],ten_nodes[j],5,positions)
            astar_time.append((ten_nodes[i],ten_nodes[j],astar_path[0]))
    # print(dfs_time)
    # print(ucs_time)
    return (dfs_time,ucs_time,astar_time)
def plot_time_graph(graph):
    dfs,ucs,astar= random_path_finder(graph)
    fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(10, 5))
    
    # Plot for dfs
    x1 = [f"{t[0]}->{t[1]}" for t in dfs]
    y1 = [t[2] for t in dfs]
    ax1.scatter(x1, y1)
    ax1.set_xticklabels(x1, rotation=90, fontsize=5)
    ax1.set_xlabel("a -> b")
    ax1.set_ylabel("Time in Ms")
    ax1.set_title("Time taken between two nodes (dfs)")

    # Plot for ucs
    x2 = [f"{t[0]}->{t[1]}" for t in ucs]
    y2 = [t[2] for t in ucs]
    ax2.scatter(x2, y2)
    ax2.set_xticklabels(x2, rotation=90, fontsize=5)
    ax2.set_xlabel("a -> b")
    ax2.set_ylabel("Time in Ms")
    ax2.set_title("Time taken between two nodes (ucs)")

    # Plot for dfs
    x3 = [f"{t[0]}->{t[1]}" for t in astar]
    y3 = [t[2] for t in astar]
    ax3.scatter(x3, y3)
    ax3.set_xticklabels(x3, rotation=90, fontsize=5)
    ax3.set_xlabel("a -> b")
    ax3.set_ylabel("Time in Ms")
    ax3.set_title("Time taken between two nodes (A* Search)")

    plt.show()
plot_time_graph(graph_1)
