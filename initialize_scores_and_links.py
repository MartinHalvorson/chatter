import wikipedia
import json
import re

# Selects number of Wikipedia articles to add
number_of_articles = 11

# Loads dictionary of most common words from basics_counts.txt
with open("scores.txt", "r") as file_name:
    scores = json.load(file_name)

with open("links.txt", "r") as file_name:
    links = json.load(file_name)

with open("basics.txt", "r") as file_name:
    basics = json.load(file_name)

for i in range(number_of_articles):
    try:
        # Uses Wikipedia API to get random article (object)
        title = wikipedia.random(1)

        # Prints article number and title
        print(str(i + 1) + ". " + title)

        # Creates string of lowercase text from Wikipedia article
        article_text = wikipedia.page(title).content.lower()
        article_text = "this is a test sentence for analysis is a test"

        # Creates list of words in article
        words = re.findall("[0-9A-z']+", article_text)

        # UPDATING LINKS DICTIONARY
        # Iterating through each word and its following word
        for j in range(len(words) - 1):

            # Renaming for code clarity
            first_word = words[j]
            second_word = words[j + 1]

            # Extracts first word's dictionary from links dictionary
            connected_words = links.get(first_word, {})

            # Increments previous value of second word in the first word's dictionary
            connected_words[second_word] = connected_words.get(second_word, 0) + 1

            # Puts first words's dictionary back into links dictionary
            links[first_word] = connected_words

        # UPDATING SCORES DICTIONARY
        for word in basics



    # Occasional errors retrieving file
    except:
        print("Error, skipping " + title)

    # Updates basics.txt file with most recent list every nth times (n = 5 below)
    if i % 10 == 0:

        # Dumps list in json format into basics.txt file
        with open('links.txt', 'w') as file_name:
            json.dump(links, file_name)

        # Updates basics_counts.txt to reflect updated dictionary (building over time instead of erasing after run)
        with open("scores.txt", "w") as file_name:
            json.dump(scores, file_name)
