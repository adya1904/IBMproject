import nltk
from nltk import tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from synonyms import synonym
from parse_yaml_file import parse_yaml

ps = PorterStemmer()

def get_endpoint(user_story, yaml_file):
    stopWords = set(stopwords.words('english'))
    words = word_tokenize(user_story)
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)
    tagged = nltk.pos_tag(wordsFiltered)

    parse_yaml_response = parse_yaml(yaml_file)

    get = ["see","search","observe","get","identify","detect","view","informed"]
    post = ["add","include","upload","annotate"]
    put = ["update","change","edit","filter"]
    delete = ["remove", "delete"]
    req_action=[]

    for i in range(len(tagged)):
        if tagged[i][0] in (set(synonym(get))):
            req_action.append(tagged[i])
            req_action.append("get")

        elif tagged[i][0] in (set(synonym(post))):
            req_action.append(tagged[i])
            req_action.append("post")
        
        elif tagged[i][0] in (set(synonym(put))):
            req_action.append(tagged[i])
            req_action.append("put")
            
        elif tagged[i][0] in (set(synonym(delete))):
            req_action.append(tagged[i])
            req_action.append("delete")
    
    #print(req_action)

    common_endpoint_tokens = [] 
    for endpoint in parse_yaml_response:
        splitted_endpoint = endpoint.split("/")
        del splitted_endpoint[0]
        lem_endpoint = []
        lem_common_words = []
        for j in range(len(tagged)):
            lem_common_words.append(ps.stem(tagged[j][0]))
        for k in splitted_endpoint:
            lem_endpoint.append(ps.stem(k))
        for i in lem_common_words:
            if i in lem_endpoint:
                common_endpoint_tokens.append(i)
    filtered_common_endpoint_tokens = list(set(common_endpoint_tokens))

    for endpoint in parse_yaml_response:
        splitted_endpoint = endpoint.split("/")
        del splitted_endpoint[0]
        lem_endpoint = []
        for k in splitted_endpoint:
            if k.startswith("{"):
                pass
            else:
                lem_endpoint.append(ps.stem(k))
        set_difference=set(lem_endpoint).symmetric_difference(set(filtered_common_endpoint_tokens))
        if not set_difference:
            find_method(endpoint,req_action[1],parse_yaml_response)

def find_method(endpoint1,check_method,parse_yaml_response):
    endpoint_dict = dict()
    for endpoint in parse_yaml_response:
        #s = "/"+endpoint1
        if endpoint == endpoint1:
            for method in parse_yaml_response[endpoint]:
                if method == check_method:
                    endpoint_dict.update({endpoint:[method,parse_yaml_response[endpoint][method]]})
                    print(endpoint_dict)
    #                 print(endpoint," : " ,method)
    #                 print(parse_yaml_response[endpoint][method])
    # print()

# data = "As a user, I want to identify persons in videos, and receive related information about them."
# get_endpoint(data,"swagger(6).yaml")