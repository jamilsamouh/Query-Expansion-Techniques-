import gensim
m_word2vec = gensim.models.KeyedVectors.load_word2vec_format('wiki-news-300d-1M.vec')
from nltk.stem import PorterStemmer
def word2vec_query_expansion(query,k):
    upd_query=get_tokenized_list(query)[0]
    synonyms =[]
    res=[w for w in upd_query]
    ps = PorterStemmer()
    for q in upd_query:
        q_stem=ps.stem(q)
        if q in m_word2vec.vocab:
            w=m_word2vec.most_similar(positive=[q],topn=k)
            for u,v in w:
                u_stem=ps.stem(u)
                if  u_stem!=q_stem:
                      res.append(u)
#     print(' '.join(res))
    return ' '.join(res)