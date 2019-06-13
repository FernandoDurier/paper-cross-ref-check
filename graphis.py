import json
import os
paperdirectory = "/Users/fernandodurier/Desktop/sarcasm-paper-review"
data=[]

def graphPapers(papers):
    ##
    # clean-authors 
    # clean-refs 
    # title 
    # path.split('\/')[len(path.split('\/'))]
    vertrixes=[] #set of works
    edges=[] #set of tuples, (source, target) 
    jedges=[] #set of edges for jgraph lib
    jvertrixes={} #set of edges for jgraph lib
    for p in papers:
        ptitle=p['title']
        if ptitle:
            ptitle=ptitle.replace('\n', ' ')
            ptitle=ptitle.strip().lstrip().rstrip()

        vertrixes.append(ptitle)

        for r in p['clean-refs']:
            rtitle=r['title']
            if rtitle:
                rtitle=rtitle.replace('\n', ' ')
                rtitle=rtitle.strip().lstrip().rstrip()

            if rtitle not in vertrixes:
                vertrixes.append(rtitle)
            
            ptuple=(vertrixes.index(ptitle), vertrixes.index(rtitle))
            jgraphdict={"source":vertrixes.index(ptitle), "target":vertrixes.index(rtitle)}
            if vertrixes.index(ptitle) not in jvertrixes:
                jvertrixes[vertrixes.index(ptitle)] = {'name':ptitle,'path':p['path'],'color': 0xffaaaa, 'size': 3.0}
            if vertrixes.index(rtitle) not in jvertrixes:
                jvertrixes[vertrixes.index(rtitle)] = {'name':rtitle,'path':p['path'],'color': 0x2222ff, 'size': 1.50}
            if jgraphdict not in jedges:
                jedges.append(jgraphdict)
            if ptuple not in edges:
                edges.append(ptuple)
    
    print("Vertrixes: ",vertrixes)
    print("Edges: ", edges)
    print("N_Vertrixes: ", len(vertrixes))
    print("N_Edges: ", len(edges))
    print("Jvertrixes:", jvertrixes)
    print("Jedges:", jedges)
    return {"edges_array":edges, "vertrix_array":vertrixes,"nodes":jvertrixes,"edges":jedges}

for root, dirs, files in os.walk(paperdirectory, topdown=False):
   for name in files:
        if "-deep.json" in name:
            with open(paperdirectory+"/"+name) as f:
                d = json.load(f)
                data.append(d)

gf = graphPapers(data)

import jgraph
jgraph.draw(gf)

# with open(paperdirectory+'/cross-ref-jgraph.json', 'w') as outfile:  
#          json.dump(gf, outfile, indent=4)

