from nytimesarticle import articleAPI
api = articleAPI('vN16ZxYzCbJ2dBe2vdVtHRfjeYiVr0lW')
articles = api.search( q = 'Indigo')

news = []
for i in articles['response']['docs']:
    dic = {}
    dic['url'] = i['web_url']
    news.append(dic)

with open('urlfile.txt', 'w') as file:
    for item in news:
        file.write('%s\n' % item)