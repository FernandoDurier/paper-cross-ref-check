import json
import os

#paperdirectory = "/Users/fernandodurier/Desktop/sarcasm-paper-review"
paperdirectory = 'C:/Users/ferna/Documents/development/paper-cross-ref-check/resources'

data=[]
cleandata=[]
for root, dirs, files in os.walk(paperdirectory, topdown=False):
   for name in files:
        if "-filtered.json" in name:
            with open(paperdirectory+"/"+name) as f:
                d = json.load(f)
                data.append(d)

for d in data:
    print('---------')
    print(d['path'])
    print('---------')
    refs=[]
    for r in d['references']:
        
        title = ''
        if '#text' in r['mixed-citation']:
            title+=(r['mixed-citation']['#text'])
        if 'article-title' in r:
            title+=(r['mixed-citation']['article-title'])

        source = None
        if 'source' in r['mixed-citation']:
            source=r['mixed-citation']['source']
        authors = ''
        if 'string-name' in r['mixed-citation']:
            author=''
            if type(r['mixed-citation']['string-name']) is list:
                for a in r['mixed-citation']['string-name']:  
                    if 'surname' in a:
                        author+=(a['surname'])
                    if 'given-name' in a:
                        author+=(', '+a['given-name'])
                    author+=(', ')
            else:
                if 'surname' in r['mixed-citation']['string-name']:
                    author+=(r['mixed-citation']['string-name']['surname'])
                if 'given-name' in r['mixed-citation']['string-name']:
                    author+=(', '+r['mixed-citation']['string-name']['given-name'])
                author+=(', ')
            authors+=author+', '
            
        reference = {"authors":authors,
        "title":title,
        "source":source}
        print(reference)
        refs.append(reference)
    d['clean-refs']=refs
    
    authors=[]
    if type(d['authors']) is list :
        for a in d['authors']:
            authors.append(a['string-name'])
    else:
        authors.append(d['authors'])
    d['clean-authors']=authors
    cleandata.append(d)

for cd in cleandata:
    filtpath=cd['path'].replace('.json','-deep')
    print(filtpath)
    with open(filtpath+'.json', 'w') as outfile:  
        json.dump(cd, outfile, indent=4, sort_keys=True)






