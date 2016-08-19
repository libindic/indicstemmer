#! /usr/bin/env python
# -*- coding: utf-8 -*-

from .util import rreplace


class Punjabi:
    '''
    Punjabi Stemmer Class
    '''

    def __init__(self):
        self.suffixes = {1: ["ੀ ਆਂ ", "िਆਂ", "ੂਆਂ", "ੀ ਏ", "ੀ ਓ"],
                         2: ["ਈ", "ੇ", "ू", "ु", "ी",
                             "ि", "ा", "ੋ", "ਜ", "ਜ਼", "ਸ"],
                         3: ["िਓ", "ਾ ਂ", "ੀ ਂ", "ੋ ਂ"],
                         4: ["ਿਉ ਂ", "ਵਾਂ", "ੀ ਆ", "िਆ", "ਈਆ"],
                         5: ["ੀ ਆ", "िਆ", "ਈਆ"]}

    def gen_replacement(self, suf, L):
        if L == 1 or L == 5:
            return suf[1:]
        return suf

    def stem(self, text):
        tag = self.suffixes.keys()
        tag.reverse()
        dic_hi = {}
        for word in text.split():
            flag = 0
            word = word.decode("utf-8")
            for L in tag:
                if flag == 1:
                    break
                if len(word) > L + 1:
                    for suf in self.suffixes[L]:
                        suf = suf.decode("utf-8")
                        if word.endswith(suf):
                            word1 = rreplace(word,
                                             self.gen_replacement(suf,
                                                                  L),
                                             '', 1)
                            dic_hi[word] = word1
                            flag = 1
                            break
            if flag == 0:
                dic_hi[word] = word
        return dic_hi
