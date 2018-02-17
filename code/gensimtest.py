from gensim import corpora, matutils
import mecabtest
from sklearn.ensemble import RandomForestClassifier
import os

base_path = os.path.dirname(os.path.abspath(__file__))
words = mecabtest.get_words({"it-life-hack-001.txt": "アナタはまだブラウザのブックマーク？　ブックマーク管理はライフリストがオススメ 最近ネットサーフィンをする際にもっぱら利用しているのが「ライフリスト」というサイトだ。この「ライフリスト」は、ひとことで言うと自分専用のブックマークサイトである。というよりブラウザのスタートページにするとブラウザのブックマーク管理が不要になる便利なサイトなのである。", "dokujo-tsushin-001.txt": "たとえば、馴れ馴れしく近づいてくるチャラ男、クールを装って迫ってくるエロエロ既婚男性etc…に対し「下心、見え見え〜」と思ったことはないだろうか？ “下心”と一言で言うと、特に男性が女性のからだを目的に執拗に口説くなど、イヤらしい言葉に聞こえてしまう。実際、辞書で「下心」の意味を調べてみると、心の底で考えていること。かねて心に期すること、かねてのたくらみ。特に、わるだくみ。（広辞苑より）という意味があるのだから仕方がないのかもしれない。"})
print("words")
print(words)

dictionary = corpora.Dictionary(words)
# print(dictionary.token2id)
# dictionary.filter_extremes(no_below=20, no_above=0.3)
# print(dictionary.token2id)
# dictionary.save_as_text('%s/../dict/livedoordic.txt' % base_path)
# dictionary2 = corpora.Dictionary.load_from_text('%s/../dict/livedoordict.txt' % base_path)
bows = []
for i in range(len(words)):
    bows.append(dictionary.doc2bow(words[i]))
print('vec')
print(bows)

f_vecs = [list(matutils.corpus2dense([bows[i]], num_terms=len(dictionary)).T[0]) for i in range(len(bows))]
print('f_vecs')
print(f_vecs)

label_train = [1,0]

estimator = RandomForestClassifier()

estimator.fit(f_vecs, label_train)

label_predict = estimator.predict(f_vecs)
print(label_predict)
