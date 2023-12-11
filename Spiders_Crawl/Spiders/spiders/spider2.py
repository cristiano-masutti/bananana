import scrapy

base = 'https://pitchfork.com/reviews/albums/?page={}'
class QuoteSpider(scrapy.Spider):
    name = "album2"
    start_urls = [base.format(1)]

    def parse(self, response):
        for album in response.xpath("//div[@class='review']"):
            description = album.xpath(".//a/@href").get()
            genre = album.css("div.review__meta ul.genre-list.genre-list--inline.review__genre-list li a::text").extract()

            # Initialize text_detail as an empty string
            text_detail = ""

            if description:
                # Check if the scheme is missing in the URL and add it
                if not description.startswith('http'):
                    description = response.urljoin(description)
                # Yield the request to parse_detail and use a callback to handle the result
                yield scrapy.Request(description, callback=self.parse_detail, cb_kwargs={"link": description, 'text_detail': text_detail, 'album_element': album, "genre": genre})

        # Extract the current page number from the URL
        current_page = int(response.url.split('=')[-1])

        # Generate the URL for the next page
        next_page_url = f"https://pitchfork.com/reviews/albums/?page={current_page + 1}"

        # Yield a request for the next page
        yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response, text_detail, album_element, genre, link):
        details = response.css('div.BaseWrap-sc-gjQpdd.BaseText-ewhhUZ.SplitScreenContentHeaderDekDown-csTFQR.iUEiRd.jqOMmZ.MVQMg::text').extract()
        text_detail = ' '.join(details).strip()
        artist_name = album_element.css('ul.artist-list.review__title-artist li::text').extract_first()
        album_name = album_element.css('h2.review__title-album em::text').extract_first()
        imgLink = response.css('div.SplitScreenContentHeaderLedeBlock-nUOA.cwQiEB img.ResponsiveImageContainer-eybHBd.fptoWY.responsive-image__image::attr(src)').extract_first()
        yield {'img': imgLink, 'album': album_name, 'artist': artist_name, 'genre': genre, 'description': text_detail, 'link':link}
