# !/usr/bin/python
import json
import xmltodict
import os
from codecs import open

paperdirectory = "/Users/fernandodurier/Desktop/sarcasm-paper-review"

for root, dirs, files in os.walk(paperdirectory, topdown=False):
   for name in files:
        if ".xml" in name:
            xmlfile = os.path.join(root, name)
            outputjson = xmlfile.replace("xml","json") 

            with open(xmlfile, 'r', 'ISO-8859-1') as f:
                xmlString = f.read()
                
            jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
            
            with open(outputjson, 'w') as f:
                f.write(jsonString)
