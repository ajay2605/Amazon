# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonbotItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['www.amazon.com.au/gp/bestsellers/beauty/ref=zg_bs_beauty_home_all?pf_rd_p=ff0f2cda-ecf5-40ff
                  # -8f90-6ef3ba366d49']
    start_urls = ['http://www.amazon.com.au/gp/bestsellers/beauty/ref=zg_bs_beauty_home_all?pf_rd_p=ff0f2cda-ecf5-40ff'
                  '-8f90-6ef3ba366d49/']

    def parse(self, response):
        title = response.css('.a-section .a-spacing-small').css('::attr(alt)').extract()
        price = response.css('.p13n-sc-price::text').extract()
        return AmazonbotItem(title=title,price=price)
