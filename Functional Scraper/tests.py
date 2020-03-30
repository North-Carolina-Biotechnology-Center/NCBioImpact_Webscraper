from scrape_and_create_dictionary import *

## tests for each of the functions within scrape_and_create_dictionary.py
#
## comment out each test to run it - each will run on its own
#
#
# url = 'https://www.ncbiotech.org/veterans'
# exhaustive_word_list = crawl_and_list_url_words(url)
# for item in exhaustive_word_list:
#     print(item)
#
#
# common_words_list = create_common_wordlist()
# for word in common_words_list:
#     print(word)
#
#
# test_exhaustive = ['where', 'when,', 'their', 'run/']
# test_common = ['the', 'their', 'it']
# clean_wordlist = clean_wordlist(test_common, test_exhaustive)
# for word in clean_wordlist:
#     print(word)
#
#
# test_clean = ['where', 'when', 'how', 'where', 'where', 'what', 'what']
# test_dict = create_dictionary(test_clean)
# for word, count in test_dict.items():
#     print(word, ':', count)
