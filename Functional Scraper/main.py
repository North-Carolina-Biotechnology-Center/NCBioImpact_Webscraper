# import all functions from file
from scrape_and_create_dictionary import *


# define mainline logic of program
def main():

    '''
    main line logic of the program

    1. create crawler

    2. fetch website data

    3. clean the data

    4. organize the data

    5. present the data

    '''


    ### 1. Create  Crawler && 2. Fetch Website Data ########

    # input url to scrape
    input_url = 'http://www.ncbioimpact.org/index.html'

    # define web crawler, and fetch website info, produce an exhaustive word list from website
    exhaustive_wordlist = crawl_and_list_url_words(input_url)


    ##### 3. Clean the Data ###############################

    # return a list of common words to exclude from dictionary
    common_words_list = create_common_wordlist()

    # remove common words and all symbols from exhaustive word list
    #  && return a clean word list
    clean_words_list = clean_wordlist(common_words_list, exhaustive_wordlist)

    ##### 4. Organize the Data ############################

    # create && return a dictionary in form {word: count}
    word_dict = create_dictionary(clean_words_list)

    ##### 5. Present the Data #############################

    # print each entry in the dictionary, word & word-count
    for key, value in word_dict.items():
        print(key, ":", value)

main()


### for more info, check out
#
### docs.python-guide.org/scenarios/scrape/
### www.crummy.com/software/BeautifulSoup/bs4/doc/
