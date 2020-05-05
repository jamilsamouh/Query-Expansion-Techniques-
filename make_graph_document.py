import networkx as nx
import matplotlib.pyplot as plt
def make_graph_document(list_s):
    print("Now it is graphing the text")
    G=nx.Graph()
    counter=1
    for s in list_s:
#         print(counter)
#         print(s)
        for i in range(len(s)-1):
            j=i+1
#             print(f'i equals: {i}')
            while j<len(s):
#                 print(f'j equals: {j}')
#                 print((s[i],s[j]))
#                 print(G.edges())
                if (s[i],s[j]) in G.edges():
                    G[s[i]][s[j]]['weight']+=1
                elif (s[j],s[i]) in G.edges():
                    G[s[j]][s[i]]['weight']+=1
                else:
                    G.add_weighted_edges_from([(s[i],s[j],1)])
                j+=1
        counter+=1
    print(len(G.edges()))
    G_TH=remove_nodes_from_graph(G,avg=10)
    clusters_dict=get_the_clusters(G_TH)
    print(len(G_TH.edges()))
    return clusters_dict