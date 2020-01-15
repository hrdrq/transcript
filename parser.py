# -*- coding: utf-8 -*-
import re
import pdb
d = pdb.set_trace

from pattern.en import parse
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

WORD = 0
POS = 1
CHUNK = 2
PNP = 3
LEMMA = 4

wnl = WordNetLemmatizer()

def adv_to_adj(adv):
    for ss in wn.synsets(adv):
      for lemmas in ss.lemmas(): # all possible lemmas
          for ps in lemmas.pertainyms(): # all possible pertainyms
              adj = ps.name()
              if adj[:2] == adv[:2]:
                  return adj
    return adv

def to_sentences(doc):
    res = doc.strip().split('\n')
    res = [re.sub('^- ', '', r) for r in res]
    return res

def to_words(sentence):
    res = []
    parsed = None
    while parsed is None:
        try:
            parsed = parse(sentence, lemmata=True).split()
        except:
            pass
    # parsed = parse(sentence, lemmata=True).split()
    for string in parsed:
        for data in string:
            pos = data[POS]
            if pos in [',', '.', ':']:
                continue
            word = data[LEMMA]
            if not re.search('[a-zA-Z]', word):
                continue
            # NNP: noun, proper singular
            # NNPS: noun, proper plural
            if pos in ['NNP', 'NNPS', 'NNP-LOC', 'NNPS-LOC']:
                # usually it's uppercase
                word = data[WORD][0] + word[1:]
            elif pos in ['RB']:
                word = adv_to_adj(word)
            elif pos in ['JJR', 'JJS']:
                word = wnl.lemmatize(word, 'a')
            res.append(word)
    return res
