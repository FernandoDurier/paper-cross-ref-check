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
        reference={"refid":None,"title":None}
        reference["refid"]=r["@id"]
        temptitle=""
        
        if('string-name' in r['mixed-citation']):
            if type(r['mixed-citation']['string-name']) is list:
                for sn in r['mixed-citation']['string-name']:
                    temptitle = temptitle + sn['surname']
                    if('#text' in sn):
                        temptitle = temptitle + sn['#text']
                    if('given-names' in sn):
                        temptitle = temptitle + sn['given-names']
                    temptitle = temptitle + ', '
            else:
                temptitle = temptitle + r['mixed-citation']['string-name']['surname']
                if('#text' in r['mixed-citation']['string-name']):
                    temptitle = temptitle + r['mixed-citation']['string-name']['#text']
                if('given-names' in r['mixed-citation']['string-name']):
                    temptitle = temptitle + r['mixed-citation']['string-name']['given-names']
                temptitle = temptitle + ', '
                

        if('#text' in r['mixed-citation']):
            temptitle = temptitle + r['mixed-citation']['#text'] 

        if('year' in r['mixed-citation']):
            if(type(r['mixed-citation']['year']) is list):
                temptitle = temptitle + r['mixed-citation']['year'][0] + ', '
            else:
                temptitle = temptitle + r['mixed-citation']['year'] + ', '

        if 'article-title' in r['mixed-citation']:
            if type(r['mixed-citation']['article-title']) is list:
                for at in r['mixed-citation']['article-title']:
                    temptitle = temptitle + " " + at
            else:
                temptitle = temptitle + r['mixed-citation']['article-title']
        temptitle = temptitle + ', '

        if('source' in r['mixed-citation']):
            if type(r['mixed-citation']['source']) is list:
                for s in r['mixed-citation']['source']:
                    temptitle = temptitle + s + ', '
            else:    
                temptitle = temptitle + r['mixed-citation']['source'] + ' '
        
        if('volume' in r['mixed-citation']):
            if(type(r['mixed-citation']['volume']) is list):
                for v in r['mixed-citation']['volume']:
                    temptitle = temptitle + v + ', '
            else:
                temptitle = temptitle + r['mixed-citation']['volume'] + ' '
        
        if('issue' in r['mixed-citation']):
            if(type(r['mixed-citation']['issue']) is list):
                temptitle = temptitle + '('
                for i in r['mixed-citation']['issue']:
                    temptitle = temptitle + i + ', '
                temptitle = temptitle + ')'
            else:
                temptitle = temptitle + '(' + r['mixed-citation']['issue'] + ') '
        
        if('fpage' in r['mixed-citation']):
            if(type(r['mixed-citation']['fpage']) is list):
                for f in r['mixed-citation']['fpage']:
                    temptitle = temptitle + ', ' + f
            else:
                temptitle = temptitle + ', ' + r['mixed-citation']['fpage']
        
        if('lpage' in r['mixed-citation']):
            if(type(r['mixed-citation']['lpage']) is list):
                for l in r['mixed-citation']['lpage']:
                    temptitle = temptitle + ', ' + l
            else:
                temptitle = temptitle + '-' + r['mixed-citation']['lpage']

        temptitle = temptitle.replace(', , ', ', ')
        temptitle = temptitle.replace('\n ', ' ')
        temptitle = temptitle.replace(' . ', ' ')
        temptitle = temptitle.replace('      ', ' ')
        temptitle = temptitle.replace('     ', ' ')
        temptitle = temptitle.replace('    ', ' ')
        temptitle = temptitle.replace('   ', ' ')
        temptitle = temptitle.replace('  ', ' ')
        temptitle = temptitle.strip()
        temptitle = temptitle.lstrip()
        temptitle = temptitle.rstrip()
        reference['title'] = temptitle
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






