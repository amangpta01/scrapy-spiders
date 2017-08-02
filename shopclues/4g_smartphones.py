# -*- coding: utf-8 -*-
import scrapy


class A4gSmartphonesSpider(scrapy.Spider):
    name = '4g-smartphones'
    allowed_domains = ['www.shopclues.com/mobiles-featured-store-4g-smartphone.html']
    start_urls = ['http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html']

    custom_settings = {
    	'FEED_URI' : 'tmp/shopclues.csv'
    }

    def parse(self, response):
        titles = response.css('img::attr(title)').extract()
        # images = response.css('img::attr(data-img)').extract()
        prices = response.css('.p_price::text').extract()
        discounts = response.css('.prd_discount::text').extract()

        for item in zip(titles,prices,discounts):
        	scraped_info = {
        		'title' : item[0],
        		'price' : item[1],
        		# 'image_urls' : [item[2]],
        		'discount' : item[2]
        	}

        	yield scraped_info
