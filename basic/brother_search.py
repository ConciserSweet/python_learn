# -*- coding: utf-8 -*-

import jieba
import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

text = io.open("D:\\novel\\brother.txt","rt",encoding="utf-8").read()
words = jieba.lcut(text)
counts = {}
excludes = {"他们", "自己", "没有", "两个", "一个", "起来"}

for word in words:
    if len(word) == 1:
        continue
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
#for word in excludes:
    #del counts[word]

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
