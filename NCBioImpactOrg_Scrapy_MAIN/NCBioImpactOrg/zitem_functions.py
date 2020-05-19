
def source_to_dict(soup):

    ''' takes in a BeautifulSoup Soup object, splits it up,
    and turns it into a word count dictionary, excluding
    symbols and common words '''

    for item in soup.findAll('body'):
        content = item.text.lower().split()

    all_words_list = list()
    for each in content:
        all_words_list.append(each)

    all_words_list = remove_symbols_and_commons_from(all_words_list)

    word_cts_dict = dict()
    word_used_list = list()
    for word in all_words_list:
        if word not in word_used_list:
            count = all_words_list.count(word)
            word_cts_dict[word] = count
            word_used_list.append(word)

    return word_cts_dict

def remove_symbols_and_commons_from(strings_list):

    symbols = '!@#$%^&*()_-+={[}]|\\;:"<>?/., '

    excluded_wordlist = \
    ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see',
    'come', 'think', 'look', 'want', 'give', 'use', 'find', 'tell', 'ask',
    'work', 'seem', 'feel', 'try', 'leave', 'call', 'good', 'new', 'first',
    'last', 'long', 'great', 'little', 'own', 'other', 'old', 'right',
    'big', 'high', 'different', 'small', 'large', 'next', 'early', 'young',
    'important', 'few', 'public', 'bad', 'same', 'able', 'to', 'of', 'in',
    'for', 'on', 'with', 'at', 'by', 'from', 'up', 'about', 'into', 'over',
    'after', 'the', 'and', 'a', 'that', 'I', 'it', 'not', 'he', 'as', 'you',
    'this', 'but', 'his', 'they', 'her', 'she', 'or', 'an', 'will', 'my',
    'one', 'all', 'would', 'there', 'their']

    clean_list = []

    for item in strings_list:

        # i stands for iterator; iterate the length of symbols string
        for i in range(0, len(symbols)):

            # if a item contains a symbol, erase the symbol
            item = item.replace(symbols[i], '')

        # if an item is not in excluded list, then add to clean list
        if len(item) > 0 and item not in excluded_wordlist:
            clean_list.append(item)

    return clean_list
