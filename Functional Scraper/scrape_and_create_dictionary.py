# import Python libraries and packages
# from typing import List, Any
import requests, re
from bs4 import BeautifulSoup


def crawl_and_list_url_words(url):
    ''' defines web crawler, and puts website text into a list '''

    # grabs the text from the url
    response = requests.get(url)
    source_html = response.text

    # grabs everything from the url using the Beautiful Soup Object
    soup = BeautifulSoup(source_html, 'html.parser')

    ## to find all items with tags that begin with h (for example, all headers)
    for item in soup.findAll('body'):

        # .text -- turns the everything into text,
        ## .lower() -- makes every letter lowercase,
        ## .split() -- splits each entry into it's own string
        content = item.text.lower().split()

    # build an exhaustive list of all words/items/entities
    exhaustive_url_wordlist = []
    for each_item in content:
        exhaustive_url_wordlist.append(each_item)

    # returns an exhaustive list of all words from url text
    return exhaustive_url_wordlist

def create_common_wordlist():
    ''' creates a common_words list from text file'''

    # opens the text file for reading & auto-closes the read-in file once loop is complete
    with open('common_words.txt', 'r') as common_words_file:

        # the readlines() function seperates each line into a string for parsing
        common_words = common_words_file.readlines()

        # creates a list of common words (to be excluded from our final wordcount dictionary)
        common_wordslist = [exclude_word.strip() for exclude_word in common_words]

        # returns the common words lsit
    return common_wordslist

def clean_wordlist(excluded_wordlist, exhaustive_wordlist):
    ''' exclude excluded words & all non-alpha symbols from a list'''

    # empty list to fill with words we want to keep
    clean_list = []

    for item in exhaustive_wordlist:

        symbols = '!@#$%^&*()_-+={[}]|\\;:"<>?/., '

        # i stands for iterator; iterate the length of symbols string
        for i in range(0, len(symbols)):

            # if a item contains a symbol, erase the symbol
            item = item.replace(symbols[i], '')

        # if an item is not in excluded list, then add to clean list
        if len(item) > 0 and item not in excluded_wordlist:
            clean_list.append(item)

    return clean_list


def create_dictionary(word_list):
    ''' creates a dictionary in form {word: count} '''

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict
