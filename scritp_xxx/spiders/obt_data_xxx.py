import scrapy
from scritp_xxx.repository_xvideos import insertValues


class ObtData(scrapy.Spider):
    name = "obtdata"

    def start_requests(self):
        a: int = 1
        for a in range(1, 20000):
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
            title = xvideo.css('p.title a::attr(title)').getall()
            href = xvideo.css('p.title a::attr(href)').getall()

            for t, h in zip(title,href):

                insertValues(None, t, "https://www.xvideos.com"+h, "xvideos")

