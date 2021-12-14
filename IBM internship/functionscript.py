import restapifunctions

baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'

load = {'id':'4231'}
endpoint1 = baseurl + '/song'+"/"+load["id"]
method1 = 'get'               #get API call
parameter1 = None
#create_test_script(method1, endpoint1, parameter1)    

parameter2 = {"id": "4214","additionalMetadata":"Date22/11/19","file":"songfile.mp4"}
endpoint2 = baseurl + '/song/' + parameter2['id'] + '/uploadImage'
method2 = 'post'
restapifunctions.create_test_script(method2,endpoint2,parameter2) 