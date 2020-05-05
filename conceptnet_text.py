import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests
from nltk.stem import PorterStemmer
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


def conceptnet_text_expansion_replace(text, k):
    upd_text = get_tokenized_list(text)[0]
    res = []
    ps = PorterStemmer()
    counter = 0
    for q in upd_text:
        q_stem = ps.stem(q)
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
            elif obj['edges'][i]['end']['label'].lower() == q:
                if obj['edges'][i]['start']['label'] not in res:
                    w_stem = ps.stem(obj['edges'][i]['start']['label'])
                    if w_stem != q_stem:
                        res.append(obj['edges'][i]['start']['label'])
                        counter += 1
        if counter == 0:
            res.append(q)
        counter = 0
    return ' '.join(res)

if __name__=="__main__":
    conceptnet_text=conceptnet_text_expansion_replace(text,1)
