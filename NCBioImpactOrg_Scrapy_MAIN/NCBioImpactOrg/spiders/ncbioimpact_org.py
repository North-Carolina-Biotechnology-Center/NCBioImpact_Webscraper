# -*- coding: utf-8 -*-
import scrapy as sc
from scrapy.http import Request
from scrapy.loader import ItemLoader
from NCBioImpactOrg.items import NcbioimpactOrgItem
from NCBioImpactOrg.item_functions import source_to_dict
from datetime import date
from bs4 import BeautifulSoup


class NcbioimpactOrgSpider(sc.Spider):
    name = 'ncbioimpact_org'
    allowed_domains = ['ncbioimpact.org']

    start_urls = [\
    'http://www.ncbioimpact.org/index.html',
    'http://www.ncbiotech.org'
    ]

    def parse(self, response):

        # Item['url'] is a string
        url = response.url

        # Item['wrd_cts'] is a dictionary
        source_html = response.text
        soup = BeautifulSoup(source_html, 'html.parser')
        wrd_cts_dict = source_to_dict(soup) #item_functions.py

        # Item['scrape_date'] is a date string : 'yyyy-mm-dd'
        today = date.today()

        l = ItemLoader(item=NcbioimpactOrgItem(), response=response)
        l.add_value('url', url)
        l.add_value('wrd_cts', wrd_cts_dict)
        l.add_value('scrape_date', today)
        yield l.load_item()

        ### GO TO CMD LINE

        ### ACTIVATE VIRTUAL ENVIRONMENT

        ### CD to SPIDERS FOLDER

        ### RUN scrapy crawl ncbioimpact_org -o file_name.file_type
                                # for example ncbioimpact.json
                                # can use jl, xml, csv, json

        d
