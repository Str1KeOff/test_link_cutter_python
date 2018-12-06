# coding: utf-8
import random

DATA_FILE = 'links.data'
DATA_ENCODING = 'utf-8'


def load_links_():
    try:
        with open(DATA_FILE, 'r', encoding=DATA_ENCODING) as data_file:
            return eval(data_file.read())
    except BaseException:
        return []


def save_links_():
    with open(DATA_FILE, 'w', encoding=DATA_ENCODING) as data_file:
        print(repr(links_), file=data_file)


links_ = load_links_()


def get_links():
    return links_


def generate_short_link():
    random.seed(version=2)
    while True:
        result = ''
        for i in range (7):
            cur_type = random.randint(0, 2)
            if cur_type == 0:
                result += chr(ord('a') + random.randint(0, 25))
            elif cur_type == 1:
                result += chr(ord('A') + random.randint(0, 25))
            else:
                result += chr(ord('0') + random.randint(0, 8))
        good_link = True
        for link in links_:
            if link['shorter_link'] == result:
                good_link = False
                break
        if good_link:
            return result


def add_link(link_name, link):
    links_.append({
        'link_name': link_name,
        'full_link': link,
        'shorter_link': generate_short_link()
    })
    save_links_()


def get_full_link(shorter_link):
    for cur in links_:
        if cur['shorter_link'] == shorter_link:
            return cur['full_link']
