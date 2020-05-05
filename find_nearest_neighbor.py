def find_nearest_neighbor(query,G,clusters_dict):
    print('nearet neighbor is being extracted')
#     print(G.nodes())
    upd_query=get_tokenized_list(query)[0]
#     res=[w for w in upd_query]
    res=upd_query.copy()
    print(res)
#     print(clusters_dict)
#     print(G.edges(data=True))
    for q in upd_query:
        counter=0
        print(f'The query is: {q}')
        for cluster in clusters_dict.values():
            if q in cluster:
                list_neighbors=cluster.copy()
                list_neighbors.remove(q)
                print(f'The cluster is {list_neighbors}')
                counter+=1
                break
        if counter==0:
            print('no similar neighbors')
            continue
#         print(list_neighbors)
        weight_list=[]
        for i in list_neighbors:
            print(i)
            weight_list.append((i,G.edges[(q,i)]['weight']))
#         print(weight_list)
        final_res=sorted(weight_list,key=lambda x: x[1], reverse=True)[0]
        print(f'Nearest neighbor is {final_res}')
        res.append(final_res[0])
#     print("The final query is"),
    print(f"The final query is: {' '.join(res)}")
    return  ' '.join(res)