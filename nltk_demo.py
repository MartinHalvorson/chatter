import time
start = time.clock() #print(time.clock() - start)

import nltk
import re

from nltk.tokenize import sent_tokenize, word_tokenize

#Create basics
with open("basics.txt") as fileName:
    basics = fileName.read()

#Create keywords
with open("gettysburg.txt") as fileName:
    text = fileName.read()
keywords = [x.lower() for x in re.findall("[A-z]+", text) if x.lower() not in basics]


print(words)

