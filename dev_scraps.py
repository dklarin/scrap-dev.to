import scrapy
import json


class DevtosSpider(scrapy.Spider):

    url_list = ['https://dev.to/search/feed_content?per_page=100&page=' +
                str(i) for i in range(10)]
    name = "devto"
    start_urls = url_list

    def parse(self, response):
        data = json.loads(response.text)

        dev_list = [i for i in data['result']]

        for i in range(len(dev_list)):
            yield {
                'title': dev_list[i]['title'],
                'author': dev_list[i]['user']['name'],
                'tag_list': dev_list[i]['tag_list'],
                'date': dev_list[i]['readable_publish_date'],
                'reading_time': dev_list[i]['reading_time']
            }
