import scrapy
from JeopardyProject.items import GameSummary
from scrapy.loader import ItemLoader

class GamesSpider(scrapy.Spider):
    name = 'games'

    start_urls = [
        'http://www.j-archive.com/showgame.php?game_id=1062',
        'http://www.j-archive.com/showgame.php?game_id=6233',
        'http://www.j-archive.com/showgame.php?game_id=2775',
        'http://www.j-archive.com/showgame.php?game_id=3578',
        'http://www.j-archive.com/showgame.php?game_id=1101'
    ]
    
    def parse(self, response):
        contestants = response.css('p.contestants')
        loader = GameSummary()
        loader['game_id'] = response.xpath('//div[@id = "game_title"]//text()').get()
        loader['game_comments'] = response.xpath('//div[@id = "game_comments"]//text()').extract()
        loader['contestant_1'] = contestants[0].css('a::text').get()
        loader['contestant_1_bio'] = contestants[0].xpath('text()').get()
        loader['contestant_2'] = contestants[1].css('a::text').get()
        loader['contestant_2_bio'] = contestants[1].xpath('text()').get()
        loader['returning_champion'] = contestants[2].css('a::text').get()
        loader['returning_champion_bio'] = contestants[2].xpath('text()').get()
        scores = response.xpath('//td[@class = "score_positive" or @class = "score_negative"]//text()').extract()
        loader['rc_score_J'] = scores[3]
        loader['c_2_score_J'] = scores[4]
        loader['c_1_score_J'] = scores[5]
        loader['rc_score_DJ'] = scores[6]
        loader['c_2_score_DJ'] = scores[7]
        loader['c_1_score_DJ'] = scores[8]
        loader['rc_score_F'] = scores[9]
        loader['c_2_score_F'] = scores[10]
        loader['c_1_score_F'] = scores[11]
        yield loader

        for a in response.xpath('//a[contains(text(), "next game")]/@href'):
            yield response.follow(a, self.parse)



            
