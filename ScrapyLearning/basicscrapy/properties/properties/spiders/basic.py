import re
import scrapy
from scrapy.selector import Selector
from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["cnbc.com"]
    start_urls = ["https://www.cnbc.com/make-it/earn/"]

    def parse(self, response):
        self.log("Got blocks")

        blocks = response.xpath("//div[@data-test = 'ThreeUpCard']")

        item = PropertiesItem()

        for block in blocks:
            # block = Selector(text=block)

            title = block.xpath(".//a[contains(@class, 'title')]/text()").get()
            item['title'] = title
            self.log("title: %s" %title)

            tag = block.xpath(".//a[contains(@class, 'eyebrow')]/text()").get()
            item['tag'] = tag
            self.log("tag: %s" %tag)
            
            author = block.xpath("string(.//div[contains(@class,'footer')])").get()
            item['author'] = author
            self.log("author: %s" %author)
            
            url = block.xpath("(.//a/@href)[1]").get()
            item['url'] = url
            self.log("url: %s " %url)
            
            imageUrl = block.xpath("(.//a)[1]/div").get()

            pattern = r'background-image:url\((.*?)\)'
            match = re.search(pattern, imageUrl)
            if match:
                imageUrl = match.group(1)

            
            item['image_urls'] = imageUrl
            self.log("image url: %s " %imageUrl)

            yield item

        pass
