from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
def valid(word):
    """
    Check if input is null or contains only spaces or numbers or special characters
    """
    temp = re.sub(r'[^A-Za-z ]', ' ', word)
    temp = re.sub(r"\s+", " ", temp)
    temp = temp.strip()
    if temp != "":
        return True
    return False
import urllib
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
def thesaurus(word,k,pos="noun"):
        """
        Fetches the synonyms from the thesaurus.com using Beautiful Soup
        """
        try:
            if pos == "noun":
                response = urlopen('http://www.thesaurus.com/browse/{}/noun'.format(word))
                print(response)
            elif pos == "verb":
                response = urlopen('http://www.thesaurus.com/browse/{}/verb'.format(word))
            elif pos == "adj":
                response = urlopen('http://www.thesaurus.com/browse/{}/adjective'.format(word))
            else:
                raise PosTagError('invalid pos tag: {}, valid POS tags: {{noun,verb,adj}}'.format(pos))
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'lxml')
            counter=0
#                 print(soup)
            result = []
#                 print(soup.findAll('div', {'id': 'synonyms-0'}))
#             print(soup.findAll('ul',{'class':"css-1lc0dpe et6tpn80"})[0])
#             print(type(soup.findAll('ul',{'class':"css-1lc0dpe et6tpn80"})[0]))
            for s in str(soup.findAll('ul',{'class':"css-1lc0dpe et6tpn80"})[0]).split():
                if s[:4]=='href' and counter<k:
#                     print(s)
                    counter+=1
                    start_index=s.index('>')
                    end_index=s.index('<')
                    result.append(s[start_index+1:end_index])
#             print(result)
            return result
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return []
        except urllib.error.URLError:
            print("No Internet Connection")
            return []
def get_thesaurus(query,k):
    pos_dict={'n':'noun','v':'verb','a':'adjective'}
    upd_query=get_tokenized_list(query)[0]
    print(upd_query)
    synonyms =[]
    res=[w for w in upd_query]
    for q in upd_query:
        print(q)
        if valid(q):
            pos = wordnet.synsets(q)[0].pos()
            print(thesaurus(q,k,pos_dict[pos]))
            res=res+thesaurus(q,k,pos_dict[pos])
#     print(' '.join(res))
    return ' '.join(res)

import re
