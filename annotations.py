import tagme
# Set the authorization token for subsequent calls.
tagme.GCUBE_TOKEN = "10df41c6-f741-45fc-88dd-9b24b2568a7b"
def get_annotation(query,th):
    lunch_annotations = tagme.annotate(query)
    res=[]
    # Print annotations with a score higher than 0.1
    for ann in lunch_annotations.get_annotations(th):
        res.append(ann.entity_title)
    return ' '.join(res)
if __name__=="__main__":
    annotaion_result = get_annotation(query,0.1)
