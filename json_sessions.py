import json
def get_queries_from_json(file_directory):
    with open(file_directory,'r') as my_file:
        final_res=[]
        res=[]
        for line in my_file:
            line=line.strip()
    #         print(line)
    #         line=line.strip('')
    #         print(line)
            try:
                temp=line.split(':')
    #             print(temp)
    #             print(temp[0])
                if temp[0]=='"session_id"':
    #                 print(temp[1])
                    final_res.append(res)
                    res=[]
                    res.append(temp[1][:-1].strip(' "'))
    #                 print(res)
                elif temp[0]=='"text"':
                    res.append(temp[1][:-1].strip(' "'))
    #                 print(res)
            except:
                continue
    #         final_res.append(res)
    return final_res[1:]

if __name__=="__main__":
    final_res = get_queries_from_json(file_directory)
