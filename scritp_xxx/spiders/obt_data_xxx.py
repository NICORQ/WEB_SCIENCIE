import scrapy
import urllib.request
from bs4 import BeautifulSoup
from scritp_xxx.repository_xvideos import insertValues


class ObtData(scrapy.Spider):
    name = "obtdata"

    def start_requests(self):

        for a in range(1, 20000):
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

                    soup = BeautifulSoup(page, 'html.parser')

                    tags_rew = soup.find('div', {'video-metadata video-tags-list ordered-label-list cropped'})

                    list_tags = []

                    for i in tags_rew.find_all('li'):
                        list_tags.append(i.text)

                    list_tags.remove('+')

                    del list_tags[0]

                    print(list_tags)

                    insertValues(None, k, str(list_tags), "https://www.xvideos.com" + h, "xvideos")

                    list_tags.clear()
