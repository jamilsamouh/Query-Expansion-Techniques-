from nltk.corpus import wordnet
def change_queries_1(topics_robust_directory,original_topics_file_extension,updated_topics_file_extension):
    pos_dict={'n':'noun','v':'verb','a':'adjective'}
#     directory=topics_robust_directory+'//corpus'
#     cluster_dict=extract_text_from_folder(directory)
    with open(topics_robust_directory+'//'+updated_topics_file_extension,'w') as new_file:
        with open(topics_robust_directory+'//'+original_topics_file_extension,'r') as old_file:
            for line in old_file:
                if line[:7]=='<title>':
                    query=line[8:]
#                     updated_query=word2vec_query_expansion([query])
#                     updated_query=conceptnet_query_expansion([query])
#                     updated_query=wordnet_query_expansion([query])
                    updated_query=glove_query_expansion([query])
#                     updated_query=find_similarity([q],cluster_dict)
#                     updated_query=find_nearest_neighbor([query],G,clusters_dict)
#                     updated_query=word_sense_disambiguate([query])
#                     updated_query=get_thesaurus([query])
                    print(updated_query)
                    new_file.write('<title> '+updated_query+'\n')
                else:
                    new_file.write(line)
    return None