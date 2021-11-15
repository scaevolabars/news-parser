import scrapy
from ..items import NewsItem


class KnifeSpider(scrapy.Spider):
    name = 'knife'
    start_urls = [
        'https://knife.media/tag/eco/'
    ]

    def parse(self, response, **kwargs):
        news = response.css('a.unit__content-link').xpath('@href').extract()
        print(news)
        yield from response.follow_all(news, self.parse_attr)

        pagination_links = response.css('nav.navigate a ')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_attr(self, response):
        items = NewsItem()
        items["author"] = response.css("div a.meta__item::text").get()
        items["link"] = response.url
        items['title'] = " ".join(response.css(".entry-header__title::text , em::text").extract())
        items["date"] = response.css("div span time").xpath('@datetime').extract_first()
        items["text"] = " ".join(response.css("p::text").extract())
        items["tags"] = " ".join(response.css(".tags a::text").extract())
        #items["tag_links"] = " ".join(response.css(".tags a::href").extract())
        return items

class TassSpider(scrapy.Spider):
    name = 'tass'
    start_urls = [
        'https://knife.media/tag/eco/'
    ]

    def parse(self, response, **kwargs):
        news = response.css('a.unit__content-link').xpath('@href').extract()
        print(news)
        yield from response.follow_all(news, self.parse_attr)

        pagination_links = response.css('nav.navigate a ')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_attr(self, response):
        items = NewsItem()
        items["author"] = response.css("div a.meta__item::text").get()
        items["link"] = response.url
        items['title'] = " ".join(response.css(".entry-header__title::text , em::text").extract())
        items["date"] = response.css("div span time").xpath('@datetime').extract_first()
        items["text"] = " ".join(response.css("p::text").extract())
        items["tags"] = " ".join(response.css(".tags a::text").extract())
        #items["tag_links"] = " ".join(response.css(".tags a::href").extract())
        return items