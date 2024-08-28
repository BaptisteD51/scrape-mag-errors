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


def get_headers(source):
    soup = BeautifulSoup(source, 'html.parser')
    headers = soup.select("h2")
    for index, header in enumerate(headers):
        header = header.getText()
        headers[index] = header
    return headers


def header_is_broken(header):
    regex = r" [a-zA-Z]{1}$"
    return re.search(regex, header) != None