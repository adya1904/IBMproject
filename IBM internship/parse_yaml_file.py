import json
import sys
# import pyyaml module
import yaml
from yaml.loader import SafeLoader
def parse_yaml(yaml_file):
    methods = dict()
    required_fields = ["name","in", "type", "required"]
    # Open the file and load the file
    if yaml_file.endswith((".yaml", ".yml", "json")):
        try:
            with open(yaml_file) as f:
                data = yaml.load(f, Loader=SafeLoader)
        except Exception as e:
            sys.exit(e)
    else:
        sys.exit("Sorry..!! , Not a supported file format. Provide a yaml or json file.")

    for endpoint in data['paths']:
        methods[endpoint] = dict()
        for method in data['paths'][endpoint]:
            methods[endpoint][method] = []
            for i in range(len(data['paths'][endpoint][method]["parameters"])):
                for var in data['paths'][endpoint][method]["parameters"][i]:
                    if var in required_fields:
                        methods[endpoint][method].append({var:data['paths'][endpoint][method]["parameters"][i][var]}) 
    # required_data=methods

    # with open("parsed_yaml_response","w") as json_file:
    #     json.dump(required_data,json_file, indent=2)
    return methods


