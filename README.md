# Website Scrape to Produce a Word Count Dictionary
The project is a web scraper to scrape a user input website and produce a word list & count dictionary.  See the documentation directory to view the webscrape presentation, which is a pdf of a small 6 page power point presentation describing the overall flow of the program, its modules and functions, and the purpose of each of these modules and functions.  

### Motivation
This web scraper is being built for the purposes of sensing trends in biotechnology companies within North Carolina.  Scraping key words and monitoring their occurence on different sites over time could be an indicator of these types of trends.

### Status 
This build is a work in progress.  Currently (March 3, 2020) it can scrape one file to return a dictionary of words and word counts, excluding 75 words from https://en.wikipedia.org/wiki/Most_common_words_in_English as well as any symbols or white space. 

### Style
The program is written in Python, and is extremely modular. The purpose of files, functions, and variables should be very obvious, based on naming.  There is also quite a bit of commenting. The program is intended to be continuously developed by coders who may or may not have a firm grasp of Python, and is able to be used and molded for different purposes related to web scraping.

### Tests
Tests.py is completely commented out.  Uncomment each individual section to test each function.

