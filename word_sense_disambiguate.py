from pywsd import disambiguate
def word_sense_disambiguate(query):
    query=query[0]
    print(query)
    res=[]
    disamb=disambiguate(query)
    print(disamb)
    for i,t in enumerate(disamb):
        print((i,t))
        if t[1] is not None:
            res.append(t[0])
            x=t[1].name().split('.')
            y=x[0].split('_')
            if t[0].lower() != (' '.join(y)).lower():
                res=res+y
        else:
            res.append(t[0])
#     print(' '.join(res))
    return ' '.join(res)