# Test file for running timed tests and other shenanigans

import wikipedia
import time

'''
10.2 seconds to get 10 articles individually
4.1 seconds to get 10 articles together

'''

open("links.txt", 'a')
loops = 1
a = time.clock()

# Average of <loops> times
for i in range(loops):

    # This is the process being tested
    try:
        for j in range(1):
            titles = wikipedia.random(10)
            for title in titles:
                page = wikipedia.page(titles)
            #s = page.text
    except:
        i -= 1

print((time.clock() - a) / loops)