# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from itemloaders import ItemLoader

def clean(text):
    text = text.strip("()")
    text = ''.join(text)
    return text

def join_text(text):
    text = ''.join(text)
    return text

def test_text(text):
    return text.strip(', ')

class JeopardyClues(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_id = scrapy.Field()
    game_comments = scrapy.Field()
    clue_id = scrapy.Field()
    order_number = scrapy.Field()
    value = scrapy.Field()
    clue = scrapy.Field()
    correct_response = scrapy.Field()

class JeopardyCategories(scrapy.Item):
    game_id = scrapy.Field()
    categories = scrapy.Field()
    category_j_1 = scrapy.Field()
    category_j_2 = scrapy.Field()
    category_j_3 = scrapy.Field()
    category_j_4 = scrapy.Field()
    category_j_5 = scrapy.Field()
    category_j_6 = scrapy.Field()
    category_dj_1 = scrapy.Field()
    category_dj_2 = scrapy.Field()
    category_dj_3 = scrapy.Field()
    category_dj_4 = scrapy.Field()
    category_dj_5 = scrapy.Field()
    category_dj_6 = scrapy.Field()
    category_fj = scrapy.Field()
    category_tb = scrapy.Field()

class GameSummary(scrapy.Item):
    game_id = scrapy.Field()
    game_comments = scrapy.Field()
    contestant_1 = scrapy.Field()
    contestant_1_bio = scrapy.Field()
    contestant_2 = scrapy.Field()
    contestant_2_bio = scrapy.Field()
    returning_champion = scrapy.Field()
    returning_champion_bio = scrapy.Field()
    c_1_score_J = scrapy.Field()
    c_2_score_J = scrapy.Field()
    rc_score_J = scrapy.Field()   
    c_1_score_DJ = scrapy.Field()
    c_2_score_DJ = scrapy.Field()
    rc_score_DJ = scrapy.Field()
    c_1_score_F = scrapy.Field()
    c_2_score_F = scrapy.Field()
    rc_score_F = scrapy.Field()

class gameresponses(scrapy.Item):
    game_id = scrapy.Field()
    order_number = scrapy.Field()
    correct = scrapy.Field()
    wrong = scrapy.Field()
