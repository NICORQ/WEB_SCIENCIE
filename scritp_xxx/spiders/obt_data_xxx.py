import scrapy
from scritp_xxx.repository_xvideos import insertValues
from scritp_xxx.spiders.obt_tags import ObtTags
from scrapy.crawler import CrawlerProcess

class ObtData(scrapy.Spider):
    name = "obtdata"

    def start_requests(self):

        for a in range(1,10):
            url: str = f"https://www.xvideos.com/new/{a}"
            yield scrapy.Request(url=url, callback=self.parse)





    def parse(self, response):

        for xvideo in response.css('body'):

            title = xvideo.css('p.title a::attr(title)').getall()
            href = xvideo.css('p.title a::attr(href)').getall()

            for k,h in zip(title,href):
                k: str = k.lower()
                if ("venezuela" in k) or ("veneca" in k) or ("venezolana" in k):
                    hre: str = "https://www.xvideos.com"+h


                    tagsRaw = ObtTags.obtHref(self, hre)

                    for d in tagsRaw:
                        print( "colombia" + str(d))


                    for t, h in zip(title, href):
                        insertValues(None, t, tags, "https://www.xvideos.com"+h, "xvideos" )



