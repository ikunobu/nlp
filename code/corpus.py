#https://github.com/yasunori/Random-Forest-Example/blob/master/corpus.py
import os
import sys
import re
from gensim import corpora, matutils
import MeCab

BASE_PATH = os.path.dirname(os.path.abspath(__file__))+'/..'
DATA_DIR_PATH = '%s/data/text/' % BASE_PATH
mecab = MeCab.Tagger('mecabrc')

def get_class_id(file_name):
    '''
    ファイル名から、クラスIDを決定する。
    学習データを作るときに使っています。
    '''
    dir_list = get_dir_list()
    dir_name = next(filter(lambda x: x in file_name, dir_list), None)
    if dir_name:
        return dir_list.index(dir_name)
    return None


def get_dir_list():
    '''
    ライブドアコーパスがtext/の下にカテゴリ別にあるからそのカテゴリ一覧をとっているだけ
    '''
    tmp = ls.listdir(DATA_DIR_PATH)
    if tmp is None:
        return None
    return sorted([x for x in tmp if os.path.isdir(DATA_DIR_PATH + x)])

    
