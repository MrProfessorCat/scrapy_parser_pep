import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = (ALLOWED_DOMAIN,)
    start_urls = (f'https://{ALLOWED_DOMAIN}/',)

    def parse(self, response):
        peps_links = response.css(
            '#numerical-index').css('tr td a::attr(href)').getall()
        for link in peps_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, title = response.css('h1.page-title::text').get().split('–')
        yield PepParseItem(
            number=number.replace('PEP', '').strip(),
            name=title.strip(),
            status=response.css('dd abbr::text').get()
        )
