

base_file_name = "testAPI"
codetop = """            #common in everyfile into the top

import requests \n
import urlresponse \n
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
            f.write("    resp=urlresponse.api_call(method,endpoint,parameter)\n")
            f.write("    print(resp)\n")
            f.write(codebot)
    except Exception as error:
        print(error)
        print("file modification error")
        return
    return file           #returns the newly created file

baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'

load = {'id':'4231'}
endpoint1 = baseurl + '/song'+"/"+load["id"]
method1 = 'POST'               #get API call
parameter1 = None
#create_test_script(method1, endpoint1, parameter1)    

parameter2 = {"id": "4214","additionalMetadata":"Date22/11/19","file":"songfile.mp4"}
endpoint2 = baseurl + '/song/' + parameter2['id'] + '/uploadImage'
method2 = 'post'
create_test_script(method2,endpoint2,parameter2) 
        