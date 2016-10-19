import wikipedia
import json
import re
import requests


top_n_basic_words = 200

with open("basics_counts.txt", "r") as fileName:
    counts = json.load(fileName)
    
tally = 1

while True:
    try:
        title = wikipedia.random(1)
        print(str(tally) + ". " + title)
        for word in re.findall("[0-9A-z']+", wikipedia.page(title).content.lower()):     
            counts[word] = counts.get(word, 0) + 1
    except:
        print("Error, skipping")
    tally += 1
    if tally % 100 == 0:
        basics = [(v, k) for v, k in counts.items()]
        basics = sorted(basics, key = lambda x:x[1], reverse = True)[:top_n_basic_words]
        basics = [x[0] for x in basics]

        # Update basics
        open('basics.txt', 'w').close() # Clears file

        with open('basics.txt', 'w') as file: # Saves dictionary with 100 most common words to basics.txt as json list
            json.dump(basics, file)

        # Updates counts
        open("basics_counts.txt", "w").close()

        with open("basics_counts.txt", "w") as fileName:
            json.dump(counts, fileName)
