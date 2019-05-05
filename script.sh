#!/bin/bash
# PAPER_DIRECTORY=/Users/fernandodurier/Desktop/sarcasm-paper-review
# CERMINE_URL=http://cermine.ceon.pl/extract.do
# REQUEST_HEADER="Content-Type: application/binary"

# for filename in $PAPER_DIRECTORY/*.pdf; do
#     [ -e "$filename" ] || continue
#     base=${filename%.pdf}
#     base+=.xml
#     echo $filename
#     echo $base
#     echo "---------------------------"
#     curl -X POST --data-binary @$filename --header $REQUEST_HEADER $CERMINE_URL >> $base;
# done

python paper-metadata-extractor.py
python clean-json.py
python 1st-deep-clean.py
python graphis.py

