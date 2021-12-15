            #common in everyfile into the top


import restapifunctions 

def main(): 

    method = 'post'
    endpoint = 'https://petstore.swagger.io/v2/pet/1'
    parameter = None
    resp=restapifunctions.api_call(method,endpoint,parameter)
    print(resp)
              #common in everyfile into the bottom
if __name__ == "__main__":

          main() 