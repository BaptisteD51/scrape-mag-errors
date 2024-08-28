from functions import read_urls
from functions import get_source_code
from functions import get_headers
from functions import header_is_broken

urls = read_urls("post-urls.txt")
broken_urls = []

for url in urls:
    print(url)
    source = get_source_code(url)
    headers = get_headers(source)
    for header in headers:
        if header_is_broken(header):
            if url not in broken_urls:
                broken_urls.append(url)

f = open("broken-urls.txt",'a',encoding="utf-8")
for url in broken_urls:
    f.write(url)
    f.write('\n')

f.close()