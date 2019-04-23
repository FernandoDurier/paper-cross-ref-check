# Paper Cross-Reference Visualizer
This project is for paper correference visualization.
Using Python, bash script and in near future ... javascript.

# Running
In order to run this project and get some nice visualizations run the script.sh /bin/bash script.
Basically this set of scripts go through a directory of papers and submit each pdf file there to an CERMINE API (http://cermine.ceon.pl), that API is able to transform the PDF file into a XML of metadata and data about the paper.
With the help of the python scripts within I've transformed the xml files that are created inside the papers directory, into JSON files. 
Then, I ask the clean-json.py and 1st-deep-clean.py to organize better my metadata and finally run graphis.py.
The graphis.py script will get the cleanest JSONs and build a graph where all papers and its references become nodes in a graph and a node links to another one, if there is a citation from a paper to that other paper.
With this code, I try to find visually cross reference among my literature.

# Limitations
As is now, jgraph the library used to generate the beautiful graph is not able to label the nodes, so it is a little hard to dicern which paper is each node. That is why I'm looking for the Javascript new approach as the jgraph npm version offers such possibility.

* * example of labelling node (app)
http://patrickfuller.github.io/jgraph/examples/github.html

* * example of labelling node (code)
https://github.com/patrickfuller/jgraph/blob/master/examples/github.html