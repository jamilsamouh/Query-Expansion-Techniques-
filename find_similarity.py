from gensim.models import Word2Vec
# m_word2vec = gensim.models.KeyedVectors.load_word2vec_format('wiki-news-300d-1M.vec')
def find_similarity(q,clusters_dict):
    upd_query=get_tokenized_list(q)[0]
    res_q=[w for w in upd_query]
    print(res_q)
    most_similar=''
    cos_sim=0
    res=0
    counter=0
    for q in upd_query:
        if q not in m_word2vec.wv.vocab:
            continue
        for cluster in clusters_dict.values():
            if q in cluster:
                list_neighbors=cluster.copy()
                list_neighbors.remove(q)
#                 print(f'The cluster is {list_neighbors}')
                counter+=1
                break
        if counter==0:
            print('no similar neighbors')
            continue
        for w in list_neighbors:
            if w not in m_word2vec.wv.vocab:
                continue
            res=m_word2vec.wv.similarity(w1=q,w2=w)
            if res>cos_sim:
                cos_sim=res
                most_similar=w
        res_q.append(most_similar)
        print((cos_sim,q,most_similar))
        most_similar=''
        cos_sim=0
    print(f"The final query is: {' '.join(res_q)}")
    return  ' '.join(res_q)