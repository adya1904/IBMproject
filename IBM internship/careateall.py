#base_file_name = "testALL"


codetop = """         #common in every file # in the top of every file
import requests \n
import restapicalls\n 
def main( ):\n
"""

codebot = """                     #common in every file     #bottom of every file
if __name__ == "__main__":\n
           main() """
           
testcucumber = """
from os import name
from behave import *
import restapicalls

endpoint = None
request = None
response_code = None

baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
@given( 'I set {method} {endpoint} API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = '{endpoint}'
@given('I have valid {parameter_value} ')
def set_endpoint(context):
  global name
  name = '{parameter_value}'
@when('I send {method}HTTPS request')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= '{method}',url=baseurl+'/song/{endpoint}',load={parameter})
@then('I receive a valid HTTPS response code 200')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200
"""




def createfile(typefile,base_file_name):  #create a file
    
    if typefile == 'py':
        
        filename = base_file_name + 'auto' + ".py"#sting to store the name of the file
    if typefile == 'feature':
        filename = base_file_name + 'auto' + ".feature"    
    print(filename)    #printing file name
    try:
        

        file = open(filename, "w")   #if there is no file it will create a new file if file exixts then clear it
    except :
        print ("unable to create file")
        
    
    return file



def create_test_script(base_file_name,method, endpoint, parameter=None,baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'):     
       #calling the createfile func that returns a file
    method_check = {'get', 'post', 'put' , 'delete'}     #validation of methods
    if method.lower() not in  method_check :
        print ('this is not a correct method')
        return 
    print (type(parameter))                              #validate dictationary
    if parameter is not None and type(parameter) is not dict:          
        print("parameter is invalid")
        return

    
    
    
    try:                                   #exception handeling
        file = createfile(typefile = 'py',base_file_name = base_file_name)    
        with open(file.name, 'w') as f:    #open(file.name, w) is for writing things into the file
            f.write(codetop)               #it will append all these into the new file
            f.write("    method ='" + method + "'\n")
            f.write("    endpoint='" + endpoint + "'\n")
            f.write("    parameter=" + str(parameter) + "\n")
            f.write("    resp=restapicalls.api_call(method,endpoint,parameter)\n")
            f.write("    print(resp)\n")
            f.write(codebot)
    except Exception as error:
        print (error)
        print ("file modification error")
        return
    
    return file                    # returning the newly created file


def create_cucumber_script(base_file_name,endpoints,methods,parameter_values,parameters):
    try:                                   #exception handeling
        file = createfile(typefile = 'py',base_file_name=base_file_name)
        txt = testcucumber.format(method=methods,endpoint = endpoints, parameter_value= parameter_values, parameter = parameters)  
        print (testcucumber)  
        with open(file.name, 'w') as f:    #open(file.name, w) is for writing things into the file
            f.write (txt) 
            
                          
            
    except Exception as error:
        print (error)
        print ("file modification error")
        return
    
    return file                


def create_feature_script(file,featurename, scenarioname, endpoint, pointingattribute, methods):    
    
    try:                                   #exception handeling
            
        with open(file.name, 'a') as f:    #open(file.name, w) is for writing things into the file
                                             #it will append all these into the new file
            f.write ("Feature: " + featurename +"\n")    #appending strings into the file

            f.write("Scenario: " + scenarioname +"\n")

            f.write("Given I set " + methods +' ' + endpoint + " API endpoint" +" \n")

            f.write("And I have valid " + pointingattribute +"\n")

            f.write("When I send"+ methods +" HTTPS request\n")

            f.write("Then I receive a valid HTTPS response code 200\n")  

            f.write("Examples:\n")
    except Exception as error:
        print (error)
        print ("file modification error")
        return
    
    return file                    # returning the newly created file

def create_file(baseurl=None,typescript = None,projectid=None,userstoryid= None,method=None, endpoint=None, parameter=None,parameter_values=None,featurename=None, scenarioname=None, pointingattribute=None):
    if typescript == 'testscript':           
        base_file_name = "testAPI"+projectid+userstoryid
        create_test_script(baseurl=baseurl,base_file_name=base_file_name,method=method, endpoint= endpoint, parameter=parameter)
    if typescript == 'stepsscript':
        base_file_name = "testcucumber"+projectid+userstoryid
        create_cucumber_script(base_file_name= base_file_name,endpoints=endpoint,methods=method,parameter_values=parameter_values,parameters=parameter)
    if typescript == 'createfeature':                            #conditionals
        base_file_name = "testfeature"+projectid+userstoryid                          #base file name
        newfile = createfile(typefile = 'feature',base_file_name = base_file_name) 
        create_feature_script(file=newfile,featurename=featurename, scenarioname=scenarioname, endpoint=endpoint, pointingattribute=pointingattribute, methods=method)
        
        
create_file(baseurl=p_baseurl,typescript = 'testscript',method=method,endpoint=req_endpoint,projectid='hello',userstoryid='world') 

#create_file(baseurl=p_baseurl,typescript = 'testscript',method=method,endpoint=req_endpoint,projectid='hello',userstoryid='world')
