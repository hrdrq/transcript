# -*- coding: utf-8 -*-
import os

from parser import to_sentences, to_words
from db import DB

def get_name(path):
    if path[-1] == '/':
        path = path[:-1]
    elif path.endswith('.txt'):
        path = path[:-4]
    return os.path.basename(path)

def get_seasons(dir_path):
    return sorted([x[0] for x in os.walk(dir_path)][1:])

def get_episodes(season_path):
    data = list(os.walk(season_path))[0]
    return [data[0] + '/' + x for x in data[2] if x.endswith('.txt')]

def count(db, season, episode, f):
    text = f.read()
    sentences = to_sentences(text)
    for sentence in sentences:
        words = to_words(sentence)
        for word in words:
            db.add(season, episode, sentence, word)

    f.close()

def main(dir_path):
    name = get_name(dir_path)
    db = DB(name)
    for season_path in get_seasons(dir_path):
        for episode_path in get_episodes(season_path):
            season = get_name(season_path)
            episode = get_name(episode_path)
            count(db, season, episode, open(episode_path))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    a = parser.parse_args()

    main(a.path)
