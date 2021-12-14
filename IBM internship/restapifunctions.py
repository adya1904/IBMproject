import requests

def get_api(url, load):
    response_code = -1            #to store the status code later
    output = ''                   #to store jason or text format of the response
    try:
        response_get = requests.get(url, params = load, timeout = 10, verify = True)  #GET API call
        response_code = response_get.status_code      #store the status code from response_get
        output = response_get.json()
    except Exception as error:
        print(error)
        return response_code
    print(response_code)
    return output

def post_api(url, pload):
    response_code = -1
    output = ''
    try:
        response_post = requests.post(url, data = pload, timeout = 10, verify = True)
        response_code = response_post.status_code
        output = response_post.json()
    except Exception as error:
        print(error)
        return response_code
    print(response_code)
    return output

def delete_api(url, pload):
    response_code = -1
    output = ''
    try:
        response_delete = requests.delete(url, data = pload, timeout = 10, verify = True)
        response_code = response_delete.status_code
        output = response_delete.text
    except Exception as error:
        print(error)
        return response_code
    print(response_code)
    return output

def put_api(url, params):
    response_code = -1
    output = ''
    try:
        response_put = requests.put(url, data = params, timeout = 10, verify = True)
        response_code = response_put.status_code
        output = response_put.text
    except Exception as error:
        print(error)
        return response_code
    print(response_code)
    return output
    
def api_call(method,url,load):            #check all the methods and call respective functions
    method = method.lower()
    if method == 'get':
        return(get_api(url,load))
    
    if method == 'post':
        return(post_api(url,load))
    
    if method == 'put':
        return(put_api(url,load))
    
    if method == 'delete':
        return(delete_api(url))
    
    
    
    
    
base_file_name = "testAPI"
codetop = """            #common in everyfile into the top


import restapifunctions \n
def main(): \n
"""
    
codebot = """              #common in everyfile into the bottom
if __name__ == "__main__":\n
          main() """
          
def createfile():          #function to create a new file
    filename = base_file_name + 'auto' + ".py"        #to store the file name
    print(filename)
    try:
        file = open(filename, "a")  #open is a function with stingparameter a to create a file
    except:
        print("unable to create file")
    return file

def create_test_script(method,endpoint,parameter):    #validation of method
    method_check = {'get','post','put','delete'}      #method_check is a set
    if method.lower() not in method_check:
        print('this is not the correct method')
        return
    print(type(parameter))                              #validation of dictationary
    if parameter is not None and type(parameter) is not dict:
        print ("parameter is invalid")
        return
    
    try:
        file = createfile()         #calling createfile function that will return the new file
        with open(file.name, 'w') as f:   # w string for writing contents into the new file
            f.write(codetop)
            f.write("    method = '" + method + "'\n")
            f.write("    endpoint = '" + endpoint + "'\n")
            f.write("    parameter = " + str(parameter) + "\n")
            f.write("    resp=restapifunctions.api_call(method,endpoint,parameter)\n")
            f.write("    print(resp)\n")
            f.write(codebot)
    except Exception as error:
        print(error)
        print("file modification error")
        return
    return file           #returns the newly created file

