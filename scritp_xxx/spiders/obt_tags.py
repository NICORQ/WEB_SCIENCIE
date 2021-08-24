import scrapy

class ObtTags(scrapy.Spider):
    name = "obtTags"



    def start_requests(self, href):
        print("hola")
        url: str = href
        yield scrapy.Request(url=url, callback=self.parse1)


    def parse1(self, response):
        print("No paso por aqui")
        for xtags in response.css('body'):
            print( "pruebas" + xtags)
            return {xtags.css('a.btn.btn-default')}

