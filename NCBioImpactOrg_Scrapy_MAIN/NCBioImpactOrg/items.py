import scrapy as sc
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags, replace_escape_chars


class NcbioimpactOrgItem(sc.Item):
    url = sc.Field() # a string
    wrd_cts = sc.Field() # a dictionary
    scrape_date =  sc.Field() # 'yyyy-mm-dd'
