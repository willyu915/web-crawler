import requests, json
url = "https://gateway.reddit.com/desktopapi/v1/subreddits/Music?rtj=only&redditWebClient=web2x&app=web2x-client-production&allow_over18=1&include=identity&after=t3_takbst&dist=10&forceGeopopular=false&layout=compact&sort=hot"
headers = {"Host": "gateway.reddit.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
            "Accept": "teext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
            "TE": "trailers"}

res = requests.get(url,headers = headers)

data = json.loads(res.text)
with open("test.json", "w") as file:
	json.dump(data, file)
posts_dict = data ['posts']

    
out_list = []
for i in posts_dict.values():
    comments = i.get('numComments','comments not found')
    tag = i['flair'][0]['richtext'][0]['t']
    link = i['media'].get('richtextContent', 'link not found')
    if link == 'link not found':
        link = i['source']['url']
    else:
        link = link['document'][0]['c'][0]['t']
    # out_list.append([comments, tag, link])
    print([comments, tag, link])

print(out_list)

