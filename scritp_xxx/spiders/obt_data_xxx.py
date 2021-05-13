import scrapy


class ObtData(scrapy.Spider):
    name = "obtdata"

    def start_requests(self):
        a: int = 1
        for a in range(5):
            url: str = f"https://www.xvideos.com/new/{a}"
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #    page = response.url.split("/")[-1]
    #   filename = 'xvideos-%s.html' % page
    #  with open(filename, 'wb') as f:
    #     f.write(response.body)
    # self.log('Saved file %s' % filename)

    def parse(self, response):
        for xvideo in response.css('body'):
            yield {
                'text': xvideo.css('p  a').getall(),
            }