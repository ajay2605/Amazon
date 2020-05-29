# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonDotComItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['https://www.amazon.com.au/gp/bestsellers/?ref_=nav_cs_bestsellers']
    start_urls = ['https://www.amazon.com.au/gp/bestsellers/beauty/ref=zg_bs_beauty_home_all?pf_rd_p=ff0f2cda-ecf5-40ff'
                  '-8f90-6ef3ba366d49/']

    def parse(self, response):
        title = response.css('.a-section .a-spacing-small').css('::attr(alt)').extract()
        price = response.css('.p13n-sc-price::text').extract()
        return AmazonDotComItem(title=title, price = price)
