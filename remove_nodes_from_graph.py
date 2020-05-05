def remove_nodes_from_graph(G,avg):
    G=G.copy()
#     total=0
#     counter=0
    print(len(G.edges()))
    print('It is getting the avergage')
#     for n in G.edges(data=True):
#         total+=n[2]['weight']
#         counter+=1
#         print(counter)
#     avg=total//counter
#     print(avg)
#     loop_counter=0
    for n in G.copy().edges(data=True):
        if n[2]['weight']<avg:
            G.remove_edge(n[0],n[1])
    G.remove_nodes_from(list(nx.isolates(G)))
    print(len(G.edges()))
    return G