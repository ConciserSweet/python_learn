# -*- coding: utf-8 -*-
import wordcloud
import jieba

c = wordcloud.WordCloud()
c.generate("".join(jieba.lcut("刘涛你是真滴牛逼")))
c.to_file("s.png")