#! /usr/local/bin/python

import requests

from dateutil import parser
from dateutil.tz import gettz
from lxml import etree, html

from db.tiny import MyTinyDB
from db.mongo import MongoDB

tinydb = MyTinyDB()
mongodb = MongoDB()


def string_replacer(string: str):
    string = str(string)
    list_of_strings = ['Unknown', 'Guest', 'Anonymous', 'Untitled']
    if string is None or string.lower() in (inner_str.lower() for inner_str in list_of_strings):
        string = ''

    return string


def extender(url):
    results = tinydb.get({'crawled': False})

    for paste in results:

        full_paste_object = {}
        single = paste.get('paste_id', None)

        response = requests.get('%s%s' % (url, single))

        if response.status_code == 200:

            content = response.content.decode("utf-8")

            html_document = html.document_fromstring(content)
            post_element = html_document.xpath("//div[@class='post-view']")

            username_div_element = html.fromstring(etree.tostring(post_element[0])).xpath("//div[@class='username']")
            username = html.fromstring(etree.tostring(username_div_element[0])).xpath("//a")[0].text
            full_paste_object.update({'username': string_replacer(username)})

            title_div_element = html.fromstring(etree.tostring(post_element[0])).xpath("//div[@class='info-top']")
            title = html.fromstring(etree.tostring(title_div_element[0])).xpath("//h1")[0].text
            full_paste_object.update({'title': string_replacer(title)})

            date_div_element = html.fromstring(etree.tostring(post_element[0])).xpath("//div[@class='date']")
            date = html.fromstring(etree.tostring(date_div_element[0])).xpath("//span")[0].attrib['title']
            full_paste_object.update({'date': parser.parse(date, tzinfos={'CDT': gettz("UTC")})})

            content = html.fromstring(etree.tostring(post_element[0])).xpath("//textarea[@class='textarea']")[0].text
            full_paste_object.update({'content': content.strip()})

            if mongodb.insert(full_paste_object):
                print('Crawled new', single, 'paste and saved to MONGO')
                tinydb.update({'paste_id': single})


if __name__ == '__main__':
    extender('https://pastebin.com/')
