import requests
from bs4 import BeautifulSoup
import re

def read_urls(file):
    f = open(file,'r',encoding="utf-8")
    list = f.readlines()
    for index, url in enumerate(list):
        url = url.strip()
        list[index] = url
    f.close()
    return list


def get_source_code(url):
    res = requests.get(url)
    return res.text


def get_links(source):
    soup = BeautifulSoup(source, 'html.parser')
    links = soup.select("a")
    urls = []
    for link in links:
        urls.append(link["href"])
    return urls


def url_ok(url):
    print(url)
    res = requests.get(url)
    return not res.ok


def is_valid(url):
    print(url)
    if "http" in url:
        return True


def filter_links(links):
    links = filter(is_valid, links)
    return list(links)


def filter_ok(links):
    links = filter(url_ok,links)
    return list(links)


try:
    requests.get("https://zooplus.fer/magasin")
    print("it works")
except:
    print("Doesnt' work")