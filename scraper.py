import requests
import json
import bs4 as bs
from bs4 import BeautifulSoup

headers = {
    # 'authority': 'www.ainews.com',
    'referer' : 'https://www.artificialintelligence-news.com',
    # 'referer': 'https://www.ainews.com/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'theme=dark',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

# url = 'https://www.ainews.com/p/5-ai-scams-poised-to-surge-in-2025-and-how-to-stay-safe'
url = 'https://www.artificialintelligence-news.com/news/rethinking-video-surveillance-the-case-for-smarter-more-flexible-solutions/'
response = requests.get(url, headers=headers)

print(response.status_code)

context = BeautifulSoup(response.content, 'lxml')

# print(context.prettify())

# with open('test.html', 'w') as f:
#     f.write(context.prettify())


content = context.h1.text

print(content)

section = context.find('section', {'class': 'entry-content'})
# attachment-full size-full wp-post-image
image = context.find('img',{'class':'attachment-full size-full wp-post-image'})['src']
print(image)

print(section.find('p').text)