import scrapy
import urllib.request
from bs4 import BeautifulSoup
from scritp_xxx.repository_xvideos import insertValues



class ObtData(scrapy.Spider):
    name = "obtdata"

    def start_requests(self):

        for a in range(1, 10):
            url: str = f"https://www.xvideos.com/new/{a}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for xvideo in response.css('body'):

            title = xvideo.css('p.title a::attr(title)').getall()
            href = xvideo.css('p.title a::attr(href)').getall()

            for k, h in zip(title, href):
                k: str = k.lower()
                if ("venezuela" in k) or ("veneca" in k) or ("venezolana" in k):

                    hre: str = f"https://www.xvideos.com{h}"

                    page = urllib.request.urlopen(hre)

                    soup = BeautifulSoup(page,'html.parser')
                    #tagsRaw = soup.find_all( 'div', {'class': 'video-metadata video-tags-list ordered-label-list cropped'}, 'a' )
                    tagsRew =  soup.find_all(['div' ,{'class': 'video-metadata video-tags-list ordered-label-list cropped opened'} , 'a' , { 'class':'btn btn-default'}] )


                    z = 1
                    for i in tagsRew:
                        z=z+1
                        print( str(z) + "  "+ str(i.text))

                    for t, h in zip(title, href):
                        insertValues(None, t, tags, "https://www.xvideos.com" + h, "xvideos")
