from gensim import corpora

texts = [["羽生", "竜王", "が", "藤井", "五段", "に", "負け", "ました"],
         ["羽生", "さん", "は", "金メダル", "を", "取り", "ました"]]

dictionary = corpora.Dictionary(texts)

bows = []
for i, text in enumerate(texts):
    bows.append(dictionary.doc2bow(text))

print(bows)
