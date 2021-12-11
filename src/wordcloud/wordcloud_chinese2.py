import jieba
import wordcloud

with open("唐诗三百首.txt", "r", encoding='UTF-8') as pdf_file:
    lines = pdf_file.readlines()
    cont = ''.join(lines)

wc = wordcloud.WordCloud(font_path="aoyagireisyosimo2_Regular.ttf",
                         width=1000, height=618, max_words=15)
wc.generate(" ".join(jieba.lcut(cont)))

wc.to_file("wcc2.png")
