import requests
from nltk.stem import PorterStemmer


def conceptnet_text_expansion_replace(text, k):
    upd_text = get_tokenized_list(text)[0]
    #     res=[w for w in upd_query]
    res = []
    ps = PorterStemmer()
    counter = 0
    for q in upd_text:
        q_stem = ps.stem(q)
        #         print(q)
        try:
            obj = requests.get('http://api.conceptnet.io/c/en/' + q).json()
        except:
            continue
        if len(obj['edges']) < k:
            x = len(obj['edges'])
        else:
            x = k
        for i in range(x):

            try:
                start_lan = obj['edges'][i]['start']['language']
                end_lan = obj['edges'][i]['end']['language']
            except:
                continue
            if obj['edges'][i]['start']['language'] != 'en' or obj['edges'][i]['end']['language'] != 'en':
                continue
            if obj['edges'][i]['start']['label'].lower() == q:
                if obj['edges'][i]['end']['label'] not in res:
                    w_stem = ps.stem(obj['edges'][i]['end']['label'])
                    if w_stem != q_stem:
                        res.append(obj['edges'][i]['end']['label'])
                        counter += 1
                        print(res)
            elif obj['edges'][i]['end']['label'].lower() == q:
                if obj['edges'][i]['start']['label'] not in res:
                    w_stem = ps.stem(obj['edges'][i]['start']['label'])
                    if w_stem != q_stem:
                        res.append(obj['edges'][i]['start']['label'])
                        counter += 1
                        print(res)
        if counter == 0:
            res.append(q)
        counter = 0
    #     print(' '.join(res))
    return ' '.join(res)