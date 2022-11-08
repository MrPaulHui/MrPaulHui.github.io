import datetime

with open('tags.txt', 'r', encoding='UTF-8') as f:
    tags = f.read().splitlines()
print('当前已设置的标签有：')
print(tags)
date = datetime.date.today()
print(date)
title = input('输入标题\n')
tag = input('输入标签\n')
if tag not in tags:
    with open('tags.txt', 'a', encoding='UTF-8') as f:
        f.write('\n'+tag)
text = f'---\nlayout:post\ntitle={title}\ndate:{date}\ntags:{tag}\n---'
with open(f'_posts/{date}-{title}.md', 'w') as f:
    f.write(text)