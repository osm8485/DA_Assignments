import scrapy
import re
def remove_tag(content):
    cleanr =re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext

f = open("description.txt", 'w', encoding='utf-8')

class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    start_urls = ['']

    def start_requests(self):
        with open("C:/Users/o9707/Desktop/대학교/YBIGTA/Team_DA/교육세션/DA_Assignments/0911 Crawling/scrapy_HW_2/scrapy1/urls.txt", "r") as f:
            while True:
                url = f.readline()
                #print(url)
                if not url:
                    break
                yield scrapy.Request(url=url, callback=self.get_detail)

    def get_detail(self, response):
        title = remove_tag(response.css("#container > header > div > h1").get())
        artist = remove_tag(response.css("#container > section.sectionPadding.summaryInfo.summaryTrack > div > div.basicInfo > table > tbody > tr:nth-child(1) > td > a").get())
        album = remove_tag(response.css("#container > section.sectionPadding.summaryInfo.summaryTrack > div > div.basicInfo > table > tbody > tr:nth-child(3) > td > a").get())
        play_time = remove_tag(response.css("#container > section.sectionPadding.summaryInfo.summaryTrack > div > div.basicInfo > table > tbody > tr:nth-child(4) > td > time").get())
        lyrics = remove_tag(response.css("#container > section.sectionPadding.contents.lyrics > div > div > xmp").get())
        
        f.write("제목 : " + title.strip() + "\n")
        f.write("아티스트 : " + artist.strip() + "\n")
        f.write("앨범명 : " + album + "\n")
        f.write("재생시간 : " + play_time + "\n\n")
        f.write("<가사>\n" + lyrics + "\n\n\n")
        
