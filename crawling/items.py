# -*- coding: utf-8 -*-

# Define here the models for your scraped items

from scrapy import Item, Field


class BaseItem(Item):
    appid = Field()
    crawlid = Field()
    url = Field()

class RawResponseItem(BaseItem):
    response_url = Field()
    status_code = Field()
    status_msg = Field()
    response_headers = Field()
    request_headers = Field()
    body = Field()
    links = Field()
    attrs = Field()
    success = Field()
    exception = Field()
    encoding = Field()

class Manager(BaseItem):
    _id = Field()
    name = Field()
    appointment_date = Field()
    introduction = Field()
    company = Field()
    fund_asset_size = Field()
    sex = Field()
    funds = Field()
    best_return = Field()

    image_urls = Field()
    picture = Field()

    @staticmethod
    def get_collection_name():
        return 'manager'


class Fund(RawResponseItem):
    _id = Field()
    code = Field()
    name = Field()
    type = Field()
    start_date = Field()
    end_date = Field()
    duty_days = Field()
    duty_return = Field()
    average = Field()
    rank = Field()
    manager = Field()
    company = Field()

    @staticmethod
    def get_collection_name():
        return 'fund'
