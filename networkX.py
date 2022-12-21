import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms.community import k_clique_communities


def get_data(filename):

    with open(filename, 'r', encoding='utf8') as rf:
       
        lines = rf.read().split("\n")
        data = [line.split(",") for line in lines]
        
        header = data[0]
        data = data[1:]
    
    # return header and data
    return header , data

# load data in from file
header , data = get_data("karate.csv")


# create graph object
G = nx.Graph()

for node in data:
    if len(node) == 3:
        G.add_node(int(node[0]))
        

for edge in data:
    if len(edge) == 3:
        G.add_edge(int(edge[0]), int(edge[1]))
        G[int(edge[0])][int(edge[1])]['weight'] = int(edge[2])
        G[int(edge[0])][int(edge[1])]['color'] = 'grey'

#store the degree of each node
maxTable = []
max_ = 0
max_degree_node=0
for node in G.nodes:
    G.nodes[node]['color'] = 'green'
    maxTable.append({'node' : node , 'num': G.degree[node]})
    if G.degree[node] >= max_:
        max_ = G.degree[node]
        max_degree_node = node
        
sorted_list = sorted(maxTable,key=lambda x:x['num'],reverse=True)

i = 0
valuesofdegrees = [] # for d)

for row in sorted_list:
    valuesofdegrees.append(list(row.values())[1])
    i=i+1
    if i == 10:
        break



# visualize graph
def visualize():
    
    pos = nx.spring_layout(G)

    edge_colors = nx.get_edge_attributes(G,'color').values()
    node_colors = nx.get_node_attributes(G,'color').values()

    nx.draw_networkx(G,pos, with_labels=False, node_size=25 ,node_color = node_colors ,edge_color=edge_colors )

# metrics
def metrics():

    # b)
    print(G) #graph view 
    print('Is graph connected?',nx.is_connected(G))
    print('diameter of network : ',nx.diameter(G)) #graph diameter 
    print('average shortest path len : ',nx.average_shortest_path_length(G)) #average path len 
  
    # c)
    giant = max(nx.connected_components(G), key=len) 
    print('giant (max connected components): ', giant )
    print("giant's size : " , len(giant))
  
    # d)
    print("Max Degree :", max(valuesofdegrees), 'on node with id : ' ,max_degree_node)
    
    average = 2*G.number_of_edges() / float(G.number_of_nodes())
    print("Average Degree :", average)
 
    # e)
    print("Degree Centrality for nodes :", list(nx.degree_centrality(G).values()))

    print("Betweenness Centrality for nodes :", nx.betweenness_centrality(G, k=None, normalized=True,  endpoints=True, seed=None))

    print("Closeness_centrality for nodes :", nx.closeness_centrality(G, u=None, distance=None, wf_improved=True))

    print("Eigenvector Centrality for nodes :", list(nx.eigenvector_centrality(G, max_iter=5000, tol=1e-06, nstart=None, weight=None).values()))
  
    # f)
    print("Average clustering coefficient for network :", round(nx.average_clustering(G),4))

    print("Number of triangles for network :",nx.triangles(G))

    #print("Clustering coefficient distribution:", round(nx.clustering(G, weight=None).values() , 4))
    
    # g)

    print("Bridges of network :",list(nx.bridges(G)))

    print("Local Bridges of network:",list(nx.local_bridges(G, with_span=True, weight=None)))
   
    # h)
    print("Graph density : " , nx.density(G))
  
    # i)
    #print("Greedy_modularity_communities: " , len(list(community.girvan_newman(G))))

    print("K_clique_communities: " , list(k_clique_communities(G , 2)))
   
    #k)
    print("Pagerank: " , nx.pagerank(G))


metrics()
visualize()


# a)
plt.savefig('graph.png')
plt.show()
