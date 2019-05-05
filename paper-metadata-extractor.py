import json
import xmltodict
import os
#from codecs import open
import requests
from lxml.etree import fromstring

PAPER_DIRECTORY='C:/Users/ferna/Desktop/sarcasm-paper-review'
FILE_OUTPUT='C:/Users/ferna/Documents/development/paper-cross-ref-check/resources'
CERMINE_URL='http://cermine.ceon.pl/extract.do'
REQUEST_HEADER={"Content-Type": "application/binary"}

print("------------------------------------------------------")
for root, dirs, files in os.walk(PAPER_DIRECTORY, topdown=False):

   pdffiles = [a for a in files if '.pdf' in a]
   progress = len(pdffiles)
   elapsed = 0

   for name in pdffiles:
       print("Progress: ", elapsed+1, "/", progress)
       elapsed = elapsed + 1       
       filename = name
        
       jsonfileoutputname = FILE_OUTPUT+'/'+filename.replace(".pdf",".json")
       xmlfileoutputname = FILE_OUTPUT+'/'+filename.replace(".pdf",".xml")
       fullpdfurl = PAPER_DIRECTORY+'/'+filename

       paperfile = open(fullpdfurl, 'rb')
        
       response = requests.post(CERMINE_URL,data=paperfile,headers=REQUEST_HEADER)
       responsexml = fromstring(response.content.decode('ISO-8859-1').encode('utf-8'))
       jsonString = json.dumps(xmltodict.parse(response.content.decode('ISO-8859-1').encode('utf-8')), indent=4)
        
       with open(jsonfileoutputname, 'w') as f:
           f.write(jsonString)
       with open(xmlfileoutputname, 'w') as x:
           x.write(response.content.decode('ISO-8859-1'))
       print("--------------------------------------------------------------------")


