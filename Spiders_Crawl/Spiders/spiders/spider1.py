import scrapy

class QuoteSpider(scrapy.Spider):
    name = "album1"
    start_urls = ["https://www.discogs.com/search/?type=all"]

    def parse(self, response):
        for album in response.xpath("//li[@role='listitem']"):
            description = album.xpath(".//a/@href").get()
            
            # Initialize text_detail as an empty string
            text_detail = ""

            if description:
                # Check if the scheme is missing in the URL and add it
                if not description.startswith('http'):
                    description = response.urljoin(description)
                # Yield the request to parse_detail and use a callback to handle the result
                yield scrapy.Request(description, callback=self.parse_detail, cb_kwargs={"link": description, 'text_detail': text_detail, 'album_element': album})

        next_page = response.xpath("//a[@class='pagination_next']/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response, text_detail, album_element, link):
        details = response.css('div.notes_1LXvZ::text').extract()
        text_detail = ' '.join(details).strip()
        specific_element = response.css('table.table_1fWaB tbody tr:nth-child(5) td a::text').extract()
        album_name = album_element.css('a.search_result_title::text').extract_first()
        artist_name = album_element.css('div.card-artist-name a::text').extract_first()
        imgLink = response.css('div.image_3rzgk.bezel_2NSgk img::attr(src)').extract_first()
        yield {'img': imgLink, 'link': link, 'album': album_name, 'artist': artist_name, 'genre': specific_element, 'description': text_detail}

# To run the spider, you can use the command: scrapy crawl album1
