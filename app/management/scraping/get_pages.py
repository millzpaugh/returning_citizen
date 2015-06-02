#!/usr/bin/env python

import requests
from lxml import html
import re
import os
import codecs

URL = 'http://www.cjccresourcelocator.net/ResourceLocator/List.aspx'


def helper_fields(html_text):
    tree = html.fromstring(html_text)
    ids = ['__VIEWSTATE', '__EVENTVALIDATION']
    result = {id: tree.xpath('//input[@id="'+id+'"]/@value')[0]
              for id in ids}
    result['__EVENTARGUMENT'] = ''
    return result


def targets_from(html_text):
    return re.findall("doPostBack\('(.+?)'", html_text)


def get_page(target, context):
    context.update({'__EVENTTARGET': target})
    result = requests.post(URL, context)
    return result.text


def write_page(html_text, filename):
    path = os.path.join('html', filename)
    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(html_text)


def main():

    base = requests.get(URL)
    base_params = helper_fields(base.text)
    base_targets = targets_from(base.text)

    for list_index, base_target in enumerate(base_targets):
        print list_index, base_target
        list_page = get_page(base_target, base_params)
        list_params = helper_fields(list_page)
        list_targets = targets_from(list_page)[35:]
        for item_index, list_target in enumerate(list_targets):
            print item_index, list_target
            result = get_page(list_target, list_params)
            filename_structure = "page{0:03d}item{1:03d}.html"
            filename = filename_structure.format(list_index, item_index)
            write_page(result, filename)

if __name__ == '__main__':
    main()
