from collections import defaultdict
from community import community_louvain
def get_the_clusters(G):
    print("Now it is getting the clusters")
#     clusters=nx.clustering(G,nodes=G.nodes(),weight='weight')
    clusters = community_louvain.best_partition(G)
    print('Done clustering and now grouping the clusters')
    clusters_dic=defaultdict(list)
    counter=1
    for key,value in clusters.items():
#         print(counter)
        clusters_dic[value].append(key)
        counter+=1
    return clusters_dic