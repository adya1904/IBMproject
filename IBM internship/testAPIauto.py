            #common in everyfile into the top

import requests 

import urlresponse 

def main(): 

    method = 'post'
    endpoint = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0/song/4214/uploadImage'
    parameter = {'id': '4214', 'additionalMetadata': 'Date22/11/19', 'file': 'songfile.mp4'}
    resp=urlresponse.api_call(method,endpoint,parameter)
    print(resp)
              #common in everyfile into the bottom
if __name__ == "__main__":

          main() 