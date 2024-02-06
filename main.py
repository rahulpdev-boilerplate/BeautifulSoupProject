from bs4 import BeautifulSoup
import requests

# LOCAL HTML FILE
with open(file='website.html', mode='r', encoding="utf-8") as file:
    contents = file.read()
parser = 'html.parser'

# # YCOMBINATOR HTML FILE
# URL = 'https://news.ycombinator.com/news'
# headers = {
#
# }
# parser = 'html.parser'

# # AMAZON HTML FILE
# URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
# }
# parser = 'lxml'

# response = requests.get(url=URL, headers=headers)
# contents = response.text

soup = BeautifulSoup(contents, parser)
print(soup.prettify())

attribute = 'href'

# item = soup.find(name='h1', id='name')
# item = soup.find(name='a', rel='noreferrer')
# item = soup.select_one(selector='p a')
# item = soup.select_one(selector='#name')

# print(item)
# print(item.name)
# print(item.string)
# print(item.getText())
# print(item.get(attribute))

# items = soup.find_all(name='a', rel='noreferrer')
# items = soup.find_all(name='span', class_='score')

# for item in items:
#     print(item.getText())
#     print(item.get(attribute))
