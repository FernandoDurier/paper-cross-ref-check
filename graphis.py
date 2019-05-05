import json
import os
#paperdirectory = "/Users/fernandodurier/Desktop/sarcasm-paper-review"
paperdirectory = 'C:/Users/ferna/Documents/development/paper-cross-ref-check/resources'
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
                #"%06x" % random.randint(0, 0xFFFFFF)
                jvertrixes[vertrixes.index(ptitle)] = {'color':"C6180C", 'size': 3.0, 'title': ptitle}
            if vertrixes.index(rtitle) not in jvertrixes:
                jvertrixes[vertrixes.index(rtitle)] = {'color':"370CC6", 'size': 1.50, 'title': rtitle}
            if jgraphdict not in jedges:
                jedges.append(jgraphdict)
            if ptuple not in edges:
                edges.append(ptuple)
    
    # print("Vertrixes: ",vertrixes)
    # print("Edges: ", edges)
    # print("N_Vertrixes: ", len(vertrixes))
    # print("N_Edges: ", len(edges))
    # print("Jvertrixes:", jvertrixes)
    # print("Jedges:", jedges)
    return {"edges_array":edges, "vertrix_array":vertrixes,"jvertrixes":jvertrixes,"jedges":jedges}

for root, dirs, files in os.walk(paperdirectory, topdown=False):
   for name in files:
        if "-deep.json" in name:
            with open(paperdirectory+"/"+name) as f:
                d = json.load(f)
                data.append(d)

gf = graphPapers(data)

with open(paperdirectory+'/cross-ref-jgraph.json', 'w') as outfile:  
        json.dump(gf, outfile, indent=4)

import jgraph
jgraph.draw(gf['edges_array'])