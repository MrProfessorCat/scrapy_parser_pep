import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        numerical_index = response.css('#numerical-index')
        peps_links = numerical_index.css('tr td a::attr(href)').getall()
        for link in peps_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        regex = r'^PEP\s(?P<number>\d+)\s–\s(?P<name>.+)'
        title = response.css('h1.page-title::text').get()
        matches = re.search(regex, title)
        if matches:
            yield PepParseItem(
                number=matches.group('number'),
                name=matches.group('name'),
                status=response.css('dd abbr::text').get()
            )
