import scrapy
import re

#기존코드, 결과이상
'''
def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext 
'''   
#해결
def remove_tag(content):
    content=content.replace("\n", " ")
    cleanr =re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext

f=open('crawling.txt', 'w', encoding='utf-8')
class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    start_urls = ['https://music.bugs.co.kr/chart']

    def parse(self, response):
        for i in range(1,101):
            rank = remove_tag(response.css(f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(4) > div > strong").get())
            title = remove_tag(response.css(f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > th > p > a").get())
            artist = remove_tag(response.css(f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(8) > p > a").get())
            album = remove_tag(response.css(f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(9) > a").get())
                
            f.write("순위 : {0}, 제목 : {1}, 아티스트 : {2}, 앨범아트 : {3}\n".format(rank, title, artist, album)+ "\n")
        

