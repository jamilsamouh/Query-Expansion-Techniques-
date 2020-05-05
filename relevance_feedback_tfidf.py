import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
# topics_robust_directory='C://Users//jamil//Desktop//Research Papers//Google Query Project'

def relevance_feedback(directory):
    res=[]
    related_corpus=extract_text_from_folder(topics_robust_directory+'//corpus_test')
    bloblist=[tb(doc) for doc in related_corpus]
    for i, blob in enumerate(bloblist):
#         print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:3]:
#             print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
            res.append(word)
    return res