import feedparser
import time

RSS_URL = [
    "http://blog.livedoor.jp/dqnplus/index.rdf",
    "http://news4vip.livedoor.biz/index.rdf",
    "http://kanasoku.info/index.rdf",
    "http://blog.livedoor.jp/news23vip/index.rdf",
    "http://bipblog.com/index.rdf"
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
    html += '</ul>'
    html += '</div>'

f = open('entry.php', 'w')
f.write(html)
f.close()
