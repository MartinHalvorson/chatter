import json
import wikipedia


links = open("links.txt", 'a')
scores = open("scores.txt", 'a')
basics = open("basics.txt", 'a')


def add_topic(title):
    #try:
    page = wikipedia.page(title)
    text = page.content
    text = word_list(text)
    #except Exception:
    #    pass


def word_list(text):
    chars = ".,<>/?;:!@#$%^&*()-_=+[]{}|\n\t"
    for char in chars:
        if char in text:
            text = text.replace(char, " ")
    while "  " in text:
        text.replace("  ", " ")
    list_of_words = text.split(" ")
    for word in list_of_words:
        word = word.lower()
    print(list_of_words)
    return list_of_words


title_list = wikipedia.random(10)
for title in title_list:
    print(title)
    add_topic(title)







