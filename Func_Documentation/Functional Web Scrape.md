# Directories, Modules, Functions

C:\Users\BiotechUser\Desktop\Nickie Scrape\Website_Scrape_and_Word_Count

## Documentation Directory
C:\Users\BiotechUser\Desktop\Nickie Scrape\Website_Scrape_and_Word_Count\Documentation

### Documentation.md
C:\Users\BiotechUser\Desktop\Nickie Scrape\Website_Scrape_and_Word_Count\Documentation\Documentation.md

### Web Scrape Presentation.pdf
C:\Users\BiotechUser\Desktop\Nickie Scrape\Website_Scrape_and_Word_Count\Documentation\Web Scrape Presentation.pdf

### TO ADD: UML Diagram

## Scraper Directory
C:\Users\BiotechUser\Desktop\Nickie Scrape\Website_Scrape_and_Word_Count\Scraper

### Main.Py
C:\Users\BiotechUser\Desktop\Nickie Scrape\Website_Scrape_and_Word_Count\Scraper\Main

* main()
    1. creates a web crawler using a Beautiful Soup object, uses that object to crawl a website, and returns a list of items from the text of an input website
    2. creates a common words list, using Wikipedia's most common English words
    3. cleans the website list of common words, symbols, and white space
    4. uses the cleaned list to create a dictionary in the form {word (string): wordcount (int)}
    5. iterates through the dictionary, printing each entry as "word : wordcount"
    
### Scrape_and_Create_Dictionary.Py
C:\Users\BiotechUser\Desktop\Nickie Scrape\Website_Scrape_and_Word_Count\Scraper\scrape_and_create_dictionary.py

* crawl_and_create_word_list(url)
	* returns all items from the site, stored in a list

* create_common_word_list()
	* returns a list of common words that were copied and pasted from https://en.wikipedia.org/wiki/Most_common_words_in_English, including only the verbs, adjectives, prepositions, and others, and not the nouns from this list
 
	* may add nouns back in if these are still popping up as the most common words, I was just worried about excluding these intuitively. I don't have a logical explanation per se?

* clean_word_list(common_words_list, wordlist)
	* cleans the list of common words as well as symbols

* create_dictionary(word_list)
	* creates a dictionary in form {word: word count}


### Create_Word_Visual_Functions.Py
C:\Users\BiotechUser\Desktop\Nickie Scrape\Website_Scrape_and_Word_Count\Scraper\create_word_visual_functions.py

* WORK IN PROGRESS

