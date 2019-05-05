import json
import os

#paperdirectory = "/Users/fernandodurier/Desktop/sarcasm-paper-review"
paperdirectory = 'C:/Users/ferna/Documents/development/paper-cross-ref-check/resources'

data = []

for root, dirs, files in os.walk(paperdirectory, topdown=False):
   for name in files:
        if ".json" in name:
            print("File: ", paperdirectory+"/"+name)
            with open(paperdirectory+"/"+name) as f:
                d = json.load(f)
                filtered = {
                    'path':paperdirectory+"/"+name,
                    'title':None,
                    'abstract':None,
                    'authors':None,
                    'keywords':None,
                    'references':None,
                    'affiliation':None,
                    'pub_date':None,
                    'journal':None
                    }
                
                if 'title-group' in d['article']['front']['article-meta']:
                    filtered['title']=d['article']['front']['article-meta']['title-group']['article-title']
                else:
                    filtered['title']=None
                if d['article']['front']['article-meta']['abstract']:
                    filtered['abstract']=d['article']['front']['article-meta']['abstract']
                if 'contrib' in d['article']['front']['article-meta']['contrib-group']:
                    filtered['authors']=d['article']['front']['article-meta']['contrib-group']['contrib']
                else:
                    filtered['authors']=None
                if 'kwd-group' in d['article']['front']['article-meta']:
                    filtered['keywords']=d['article']['front']['article-meta']['kwd-group']['kwd']
                else:
                    filtered['keywords']=None
                if d['article']['back']['ref-list']:
                    filtered['references']=d['article']['back']['ref-list']['ref']
                else:
                    filtered['references']=None
                if 'aff' in d['article']['front']['article-meta']['contrib-group']:
                    filtered['affiliation']=d['article']['front']['article-meta']['contrib-group']['aff']
                else:
                    filtered['affiliation']=None
                if 'pub-date' in d['article']['front']['article-meta']:
                    filtered['pub_date']=d['article']['front']['article-meta']['pub-date']
                else:
                    filtered['pub_date']=None
                if d['article']['front']['journal-meta']:
                    filtered['journal']=d['article']['front']['journal-meta']['journal-title-group']['journal-title']
                    
                data.append(filtered)

for d in data:
    if d['references'] != None:
        filtpath=d['path'].replace('.json','-filtered')
        with open(filtpath+'.json', 'w') as outfile:  
            json.dump(d, outfile, indent=4, sort_keys=True)