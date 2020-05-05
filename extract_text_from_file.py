def extract_text_from_file(file_directory):
    with open(file_directory,'r') as my_file:
        result=[]
        lines=my_file.read().splitlines()
    #     print(lines)
        while True:
            try:
                i1=lines.index('<TEXT>')
                i2=lines.index('</TEXT>')
                result.append(' '.join(lines[i1+1:i2]))
                lines=lines[i2+1:]
            except:
                break
    #     print(' '.join(result))
#         print(result)
        print(len(result))
        return result