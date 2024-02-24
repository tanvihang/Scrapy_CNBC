# spiders functionality
# define crawling behavior for each websites
import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import QuotesToScrapeItem


# Crawler, to find related url wanted
# class CrawlingSpider(CrawlSpider):
class Crawler(CrawlSpider):
    name = "quotes.toscrape"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]


    main_page_tag = LinkExtractor(restrict_xpaths="//span[@class='tag-item']/a")
    rule_page_tag = Rule(main_page_tag, callback="parse_item", follow=False)

    rules = (
        rule_page_tag,
    )

    def parse_item(self, response):

        items = QuotesToScrapeItem()

        itemBlocks = response.xpath("//div[@class='quote']").getall()

        for itemblock in itemBlocks:

            quote=scrapy.Selector(text=itemblock).xpath("//span[1]/text()").get()
            author = scrapy.Selector(text=itemblock).xpath("//small[1]/text()").get()
            authorURL = scrapy.Selector(text=itemblock).xpath("//a[1 and @href[contains(.,'/author')]]/@href").get()
            tags = scrapy.Selector(text=itemblock).xpath("//a[1 and @href[contains(.,'/tag')]]/text()").getall()

            if(len(quote)>255):
                quote = quote[:254]
            

            items['quote'] = quote
            items['author'] = author
            items['authorUrl'] = authorURL
            items['tags'] = tags

            yield items

        next_page = response.xpath("//li[@class='next']/a/@href").get()

        if next_page is not None:
            # add into follow
            yield response.follow(next_page, callback = self.parse_item)


# to get the quote
# response.xpath("//div[@class='quote']/span[@class='text']/text()").getall()[i]
    
# to get the author
# response.xpath("//div[@class='quote']/span/small[@class='author']/text()").getall()[0] 
    
# to get the author link
# response.xpath("//div[@class='quote']/span/a/@href").getall()[0] 
    
