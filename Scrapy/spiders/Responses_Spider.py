import scrapy
from JeopardyProject.items import gameresponses
from scrapy.loader import ItemLoader

class responsesspider(scrapy.Spider):
    name = 'responses'
    start_urls = [
        'http://www.j-archive.com/showgame.php?game_id=1062',
        'http://www.j-archive.com/showgame.php?game_id=6233',
        'http://www.j-archive.com/showgame.php?game_id=2775',
        'http://www.j-archive.com/showgame.php?game_id=3578',
        'http://www.j-archive.com/showgame.php?game_id=1101'
    ]

    def parse(self, response):
        answers_url = response.xpath('//*[@id="final_jeopardy_round"]/h4/a[1]//@href').get()
        yield response.follow(answers_url, self.parse_answers)
        
        for a in response.xpath('//a[contains(text(), "next game")]/@href'):
            yield response.follow(a, self.parse)
        
    def parse_answers(self, response):
        for post in response.css('td.clue'):
            yield {
                'game_id': response.xpath('//*[@id="content"]/h1/a//text()').get(),
                'correct_response': post.css('em.correct_response').xpath('string()').get(),
                'value': post.css('td.clue_value::text,td.clue_value_daily_double::text').get() or 'FJ',
                'order_number': post.css('td.clue_order_number').css('a::text').get() or 'FJ',
                'right': post.css('td.right::text').getall(),
                'wrong': post.css('td.wrong::text').getall()
            }