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
#         print(filtered_sentence)
        filtered_sentence_unique=[x for x in filtered_sentence if not (x in seen or seen.add(x))]
#         print(filtered_sentence_unique)
        updated_list_s.append(filtered_sentence_unique)
#     print(updated_list_s)
    return updated_list_s
#     return None