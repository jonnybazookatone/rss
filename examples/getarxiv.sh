#!/bin/bash

# Usage = """ """

#__author__ = "Jonny Elliott"
#__copyright__ = "Copyright 2011"
#__credits__ =  ""
#__license__ = "GPL"
#__version__ = "0.0"
#__maintainer__ = "Jonny Elliott"
#__email__ = "jonnyelliott@mpe.mpg.de"
#__status__ = "Prototype"

python ~/workspace/journaltools/makersspage.py
python ~/workspace/journaltools/makeoldrsspage.py

python ~/workspace/journaltools/makersspage2.py
python ~/workspace/journaltools/makeoldrsspage2.py

scp ~/workspace/journaltools/*.html jonnyy@codd.uwcs.co.uk:~/public_html/feeds/
