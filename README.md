# chatter

The goal of chatter is to become a device similar to Watson (IBM) on a very small scale. Using Wikipedia articles as a database for information, chatter parses articles using the Wikipedia Python API and gathers two primary metrics: 1. a "strength of connection" between two words, or how often they appear in close proximity and 2. a list of words succeeding a given word. These two values are stored in scores.txt and links.txt respectively. initialize_scores_and_links.py initializes these two files. For functions in chatter.py, the larger these two files are (and the more information they contain) the more accurate analysis functions will be.

After analyzing an input question, the scores and links dictionaries will be used to craft sentences in response to the question. Sentences will be weighed based on confidence of answer. 

