import wikipedia
import json
import re

# Loads dictionary of most common words from basics_counts.txt
with open("scores.txt", "r") as file_name:
    scores = json.load(file_name)

with open("links.txt", "r") as file_name:
    links = json.load(file_name)

with open("basics.txt", "r") as file_name:
    basics = json.load(file_name)

def add_articles(number_of_articles):
    for i in range(number_of_articles):
        try:

            # Uses Wikipedia API to get random article (object)
            title = wikipedia.random(1)

            # Prints article number and title
            print(str(i + 1) + ". " + title)

            # Creates string of lowercase text from Wikipedia article
            article_text = wikipedia.page(title).content.lower()

            # Creates list of words in article
            list_of_words = re.findall("[0-9A-z']+", article_text)

            # UPDATING LINKS DICTIONARY
            # Iterating through each word and its following word
            for j in range(len(list_of_words) - 1):

                # Renaming for code clarity
                first_word = list_of_words[j]
                second_word = list_of_words[j + 1]

                # Extracts first word's dictionary from links dictionary
                connected_words = links.get(first_word, {})

                # Increments previous value of second word in the first word's dictionary
                connected_words[second_word] = connected_words.get(second_word, 0) + 1

                # Puts first words's dictionary back into links dictionary
                links[first_word] = connected_words

            # UPDATING SCORES DICTIONARY
            # Removes basic words from list_of_words, renames it as list_of_keywords
            list_of_keywords = [word for word in list_of_words if word not in basics]

            # Iterating through each word in keywords (avoiding some at both ends for convenience)
            for k in range(2, len(list_of_keywords) - 2):

                # Renaming for code clarity
                base_word = list_of_keywords[k]
                prior_one = list_of_keywords[k - 1]
                prior_two = list_of_keywords[k - 2]
                later_one = list_of_keywords[k + 1]
                later_two = list_of_keywords[k + 2]

                # Extracts base_words connections from scores dictionary
                connection = scores.get(base_word, {})

                # Updates surrounding word's scores in base word's dictionary
                connection[prior_two] = connection.get(prior_two, 0) + 1
                connection[prior_one] = connection.get(prior_one, 0) + 3
                connection[later_one] = connection.get(later_one, 0) + 3
                connection[later_two] = connection.get(later_two, 0) + 1

                # Puts base word's dictionary back into scores dictionary
                scores[base_word] = connection

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

add_articles(100)
