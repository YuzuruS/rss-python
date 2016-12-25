import feedparser
import time

RSS_URL = [
    "http://blog.livedoor.jp/nwknews/index.rdf",
    "http://blog.livedoor.jp/itsoku/index.rdf",
    "http://lifehack2ch.livedoor.biz/index.rdf",
    "http://workingnews.blog117.fc2.com/?xml",
    "http://burusoku-vip.com/index.rdf",
    "http://kabumatome.doorblog.jp/index.rdf",
    "http://shikaku2ch.doorblog.jp/index.rdf",
    "http://okanehadaiji.com/index.rdf",
    "http://tokkaban.com/?feed=tokka",
]

html = ''
for url in RSS_URL:
    dic = feedparser.parse(url)
    site_link = dic.feed.link
    site_title = dic.feed.title
    html += '<div class="site_entry">'
    html += '<h3>'
    html += '<a href="' + site_link + '" target="_blank">'
    html += site_title
    html += '</a>'
    html += '</h3>'
    html += '<ul>'
    cnt = 0
    for entry in dic.entries:
        title = entry.title
        link  = entry.link
        d = entry.updated_parsed
        html += '<li>'
        html += '<p class="entry_date">'
        html += time.strftime("%Y-%m-%d %H:%M", d)
        html += '</p>'
        html += '<p class="entry_title">'
        html += '<a href="' + link + '" target="_blank">'
        html += title
        html += '</a>'
        html += '</p>'
        html += '</li>'
        cnt += 1
        if cnt == 7:
            break
    html += '</ul>'
    html += '</div>'

f = open('entry.php', 'w')
f.write(html)
f.close()
