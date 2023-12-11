import scrapy
import re

class QuoteSpider(scrapy.Spider):
    name = "album3"
    start_urls = ["https://daily.bandcamp.com/album-of-the-day"]

    def parse(self, response):
        for album in response.xpath("//div[@class='list-article  aotd']"):
            description = album.xpath(".//a/@href").get()
            description = "https://daily.bandcamp.com" + description
            # Initialize text_detail as an empty string
            text_detail = ""

            if description:
                yield scrapy.Request(description, callback=self.parse_detail, cb_kwargs={"link": description,'text_detail': text_detail, 'album_element': album})

        next_page = response.xpath("//a[@class='pagination-link']/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response, text_detail, album_element, link):
        artist_album = album_element.css('a.title::text').extract_first()
        parts = artist_album.split(',')
        parts[1] = parts[1].strip()
        parts[0] = parts[0].strip()
        description = response.css('article.aotd p::text').extract()
        description = ' '.join(description)
        genre = response.css('div.genre a::text').extract()
        imgLink = response.css('article.aotd img::attr(src)').extract_first()
        yield {'img': imgLink, 'album': parts[1][1:-1], 'artist': parts[0], 'description' : description, 'genre': genre, 'link':link}
 