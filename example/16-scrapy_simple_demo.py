"""scrapy 简单的使用demo """
import os
import json
import time

from urllib.parse import parse_qs
from collections import defaultdict

import scrapy


class BlogSpider(scrapy.Spider):
    """
    nohup scrapy runspider simple_spider.py -o html_app_mi.jl \
     --loglevel=ERROR --logfile=app.mi.log \
     -a input_filename=package_name.txt \
     -a history_filename="history_data.txt" &
    """
    name = 'mi_spider'

    def start_requests(self):
        base_url = "https://sj.qq.com/myapp/detail.htm?apkName="
        with open(self.input_filename, encoding="utf8") as fr:
            urls = [base_url + f.strip() for f in fr if f.strip()]
        finish_pack = []

        if os.path.exists(self.history_filename):
            with open(self.history_filename, encoding="utf8") as fr:
                for f in fr:
                    js = json.loads(f)
                    finish_pack.append(list(js.keys())[0])

        finish_urls = [base_url + pack for pack in finish_pack]

        urls = list(set(urls) - set(finish_urls))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == 403:
            time.sleep(30)
        if response.url == "https://sj.qq.com/myapp/#":
            yield {
                "error": ""
            }
        if int(time.time()) % 60 == 0:
            time.sleep(10)

        if response.status == 200:
            dt_params = response.selector.xpath("//@dt-params").getall()
            res_dict = defaultdict(list)
            for dt_param in dt_params:
                pitems = parse_qs(dt_param)
                if "appname" in pitems:
                    key = pitems.get("appname")[0], pitems.get("pkgname")[0]
                    res_dict[key] += (pitems.get("labelname", []))
            for (app_name, package_name), value in res_dict.items():
                yield {
                    "app_name": app_name,
                    "package_name": package_name,
                    "app_label": "|".join(value)
                }
