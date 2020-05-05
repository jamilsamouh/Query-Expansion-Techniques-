import networkx as nx
from collections import defaultdict
from community import community_louvain
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def get_tokenized_list(list_s):
    print("List of words is getting tokenized right now")
    stop_words = set(stopwords.words('english'))
    l=['.',',','!','?',';','a','an','(',')',"'",'_','-']
    stop_words.update(l)
    updated_list_s=[]
    for s in list_s:
        word_tokens = word_tokenize(s)
        seen = set()
        filtered_sentence = list([w.lower() for w in word_tokens if w.lower() not in stop_words])
        filtered_sentence_unique=[x for x in filtered_sentence if not (x in seen or seen.add(x))]
        updated_list_s.append(filtered_sentence_unique)
    return updated_list_s
def make_graph_document(list_s,avg):
    print("Now it is graphing the text")
    G=nx.Graph()
    counter=1
    for s in list_s:
        for i in range(len(s)-1):
            j=i+1
            while j<len(s):
                if (s[i],s[j]) in G.edges():
                    G[s[i]][s[j]]['weight']+=1
                elif (s[j],s[i]) in G.edges():
                    G[s[j]][s[i]]['weight']+=1
                else:
                    G.add_weighted_edges_from([(s[i],s[j],1)])
                j+=1
        counter+=1
    print(len(G.edges()))
    G_TH=remove_nodes_from_graph(G,avg)
    clusters_dict=get_the_clusters(G_TH)
    print(len(G_TH.edges()))
    return G_TH,clusters_dict
def remove_nodes_from_graph(G,avg):
    G=G.copy()
    print('It is getting the avergage')
    for n in G.copy().edges(data=True):
        if n[2]['weight']<avg:
            G.remove_edge(n[0],n[1])
    G.remove_nodes_from(list(nx.isolates(G)))
    return G
def get_the_clusters(G):
    print("Now it is getting the clusters")
    clusters = community_louvain.best_partition(G)
    print('Done clustering and now grouping the clusters')
    clusters_dic=defaultdict(list)
    for key,value in clusters.items():
        clusters_dic[value].append(key)
    return clusters_dic
def term_cluster_query_expansion(query,G,clusters_dict,k):
    upd_query=get_tokenized_list([query])[0]
    res=[w for w in upd_query]
    print(res)
    for q in upd_query:
        counter=0
        print(f'The query is: {q}')
        for cluster in cluster_dict.values():
            if q in cluster:
                list_neighbors=cluster.copy()
                list_neighbors.remove(q)
                print(f'The cluster is {list_neighbors}')
                counter+=1
                break
        if counter==0:
            print('no similar neighbors')
            continue
            print(list_neighbors)
        weight_list=[]
        for i in list_neighbors:
#             print(i)
            weight_list.append((i,G.edges[(q,i)]['weight']))
    #         print(weight_list)
        final_res=sorted(weight_list,key=lambda x: x[1], reverse=True)[:k]
        print(f'List of top K terms is {final_res}')
        for u,v in final_res:
            res.append(u)
            print(f'Nearest neighbor is {u}')
        print(res)
    print(f"The final query is: {' '.join(res)}")
    return ' '.join(res)
if __name__=="__main__":
    G,cluster_dict=make_graph_document(list_s,avg)
    term_cluster_query_expansion(query, G, cluster_dict, k)