from functions import read_urls
from functions import get_source_code
from functions import get_links
from functions import filter_ok
from functions import filter_links

urls = read_urls("post-urls.txt")
error_list = []

# source = get_source_code("https://www.zooplus.fr/magazine/chien/alimentation-du-chien/alimentation-berger-australien")
# urls = get_links(source)
# urls = filter_links(urls)
# urls.append("https://zobplus.fre/magasin")
# urls = filter_ok(urls)
# for url in urls:
#     print(url)



# for url in urls:
#     print(url)
#     source = get_source_code(url)
#     headers = get_headers(source)
#     for header in headers:
#         if header_is_broken(header):
#             if url not in broken_urls:
#                 broken_urls.append(url)

# f = open("broken-urls.txt",'a',encoding="utf-8")
# for url in broken_urls:
#     f.write(url)
#     f.write('\n')

# f.close()