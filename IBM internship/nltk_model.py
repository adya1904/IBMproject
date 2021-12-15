import nltk
import json
from nltk import tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from restapifunctions import create_test_script
baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
p_baseurl = "https://petstore.swagger.io/v2"
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

    parse_yaml_response, schema = parse_yaml(yaml_file)
    print(json.dumps(schema, sort_keys=False, indent=2))

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
        else:
            set_intersection= set(lem_endpoint).intersection(set(filtered_common_endpoint_tokens))
            if not set_intersection.symmetric_difference(set(lem_endpoint)):
                find_method(endpoint,req_action[1],parse_yaml_response)
        # for method in parse_yaml_response[endpoint]:
        #     if not set_difference:
        #         if method==req_action[1]:
        #             if method=="post" or method=="put":
        #                 vch_schema = parse_yaml_response[endpoint][req_action[1]]["schema"]["$ref"].split("/")
        #                 print(json.dumps(schema[vch_schema[-1]], sort_keys=False, indent=2))
        #             print(endpoint)
        #     else:
        #         set_intersection= set(lem_endpoint).intersection(set(filtered_common_endpoint_tokens))
        #         if not set_intersection.symmetric_difference(set(lem_endpoint)):
        #             if method==req_action[1]:
        #                 print(endpoint,req_action[1],parse_yaml_response[endpoint][req_action[1]])


def find_method(endpoint1,check_method,parse_yaml_response):
    for endpoint in parse_yaml_response:
        #s = "/"+endpoint1
        if endpoint == endpoint1:
            for method in parse_yaml_response[endpoint]:
                if method == check_method:
                    # parameter2 = {"id": "4214","additionalMetadata":"Date22/11/19","file":"songfile.mp4"}
                    # endpoint2 = baseurl + '/song/' + parameter2['id'] + '/uploadImage'
                    # method2 = 'post'
                    # req_endpoint=baseurl+endpoint
                    load = {'id': "1"}
                    req_endpoint = ""
                    print(endpoint)
                    req_endpoint_lst= endpoint.split("{")
                    for i in range(len(req_endpoint_lst)):
                        if req_endpoint_lst[i].endswith("}"):
                            req_endpoint_lst[i]=load["id"]
                        req_endpoint = req_endpoint+req_endpoint_lst[i]
                    
                    endpoint1 = p_baseurl + req_endpoint
                    parameter1 = None
                    create_test_script(method,endpoint1,parameter1)
                    return(endpoint,method,parse_yaml_response[endpoint][method])

data = "I want to add and discover pet."
get_endpoint(data,"petstore.yaml")

# data = "As a user, I want to add info about perceptually similar video items."
# get_endpoint(data,"zooniverse.yaml")