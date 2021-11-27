#! /usr/local/bin/python

import requests
from datetime import datetime
from lxml import etree, html

from db.tiny import MyTinyDB

db = MyTinyDB()


def finder(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content.decode("utf-8")

        html_document = html.document_fromstring(content)
        ul_element = html_document.xpath("//ul[@class='sidebar__menu']")

        for ul_tag in ul_element:
            li_tags = html.fromstring(etree.tostring(ul_tag)).xpath("//li")

            for li_tag in li_tags:
                paste_id = li_tag.findall('a')[0].attrib['href'][1:]
                paste_obj = {
                    'paste_id': paste_id,
                    'crawled': False
                }

                results = db.get({'paste_id': paste_id})
                if len(results) == 0:
                    db.insert(paste_obj)
                    print(datetime.now(), 'Found and added new', paste_id, 'paste to temporary database')


if __name__ == '__main__':
    finder('https://pastebin.com/')
