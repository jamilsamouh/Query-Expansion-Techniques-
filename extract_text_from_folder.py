import os
def extract_text_from_folder(folder_directory):
    print("Now it is extracting the text from the folder")
    files_list = os.listdir(folder_directory)
    files_text_list=[]
    for file in files_list:
#         print(file)
        files_text_list.append(extract_text_from_file(directory+'//'+file))
    flattened_files_text_list  = [val for sublist in files_text_list for val in sublist]
#     print(flattened_files_text_list[374:376])
    print(len(flattened_files_text_list))
    tokenized_files_text_list=get_tokenized_list(flattened_files_text_list)
#     print(tokenized_files_text_list[374:376])
    cluster_dict=make_graph_document(tokenized_files_text_list)
    return cluster_dict 