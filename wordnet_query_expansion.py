from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
def wordnet_query_expansion(query,k):
    upd_query=get_tokenized_list(query)[0]
#     print(upd_query)
    ps = PorterStemmer()
    synonyms =[]
#     res=[]
    res=[w for w in upd_query]
    for q in upd_query:
        print(q)
        q_stem=ps.stem(q)
#         if q in m.vocab:
        for syn in wordnet.synsets(q):
            for l in syn.lemmas():
                synonyms.append(l.name())
        synonyms=list(set(synonyms))
        synonyms=synonyms[:k]
        print(synonyms)
        for w in synonyms:
            w_stem=ps.stem(w)
            if  w_stem!=q_stem:
                  res.append(w)
            synonyms=[]
#     print(' '.join(res))
    return ' '.join(res)