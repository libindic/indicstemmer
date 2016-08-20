#! /usr/bin/env python
# -*- coding: utf-8 -*-

from .util import rreplace


class Hindi:
    '''
    Hindi Stemmer Class
    '''

    def stem(self, text):
        suffixes = {1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
                    2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना",
                        "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
                    3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा",
                        "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता",
                        "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं", "ाएँ"],
                    4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी",
                        "ेंगी", "एंगे", "ेंगे", "ूंगी",
                        "ूंगा", "ातीं", "नाओं",
                        "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
                    5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा",
                        "ाइयाँ", "ाइयों", "ाइयां"]}
        tag = [1, 2, 3, 4, 5]
        tag.reverse()
        dic_hi = {}
        for word in text.split():
            try:
                word = word.decode("utf-8")
            except:
                pass
            flag = 0
            for L in tag:
                if flag == 1:
                    break
                if len(word) > L + 1:
                    for suf in suffixes[L]:
                        suf = suf.decode("utf-8")
                        if word.endswith(suf):
                            word1 = rreplace(word, suf, '', 1)
                            dic_hi[word] = word1
                            flag = 1
                            break
            if flag == 0:
                dic_hi[word] = word
        return dic_hi
