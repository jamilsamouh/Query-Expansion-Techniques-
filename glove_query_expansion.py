import numpy as np
import numpy
import scipy
import matplotlib
import sklearn
import gensim
from nltk.stem import PorterStemmer
def load_glove_model(glove_file):
    """
    :param glove_file: embeddings_path: path of glove file.
    :return: glove model
    """

    with open(glove_file + ".txt", 'r', encoding='utf-8') as f:
        model = {}
        print(f)
        counter=0
        for line in f:
            if counter>0:
                split_line = line.split()
                word = split_line[0]
                embedding = np.array([float(val) for val in split_line[1:]])
                model[word] = embedding
                counter+=1
            else:
                counter+=1
    return model
m_glove = load_glove_model('C://Users//jamil//Desktop//Research Papers//Google Query Project//glove.6B.300d')
def glove_query_expansion(query):
    upd_query=get_tokenized_list(query)[0]
    synonyms =[]
    res=[w for w in upd_query]
    ps = PorterStemmer()
    for q in upd_query:
        q_stem=ps.stem(q)
#         print(q)
        if q.lower() in m_glove.keys():
            w=sorted(m_glove.keys(), key=lambda word: scipy.spatial.distance.euclidean(m_glove[word],m_glove[q]))
    #         print(w)
            w=w[:3]
    #         print(w)
            for u in w:
                u_stem=ps.stem(u)
                if  u_stem!=q_stem:
                      res.append(u)
#             print(res)
#     print(' '.join(res))
    return ' '.join(res)
