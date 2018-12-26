#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .Malayalam import Malayalam
from .Hindi import Hindi
from .Punjabi import Punjabi


class Stemmer:

    def stem(self, text, language):
        if language == 'ml_IN':
            instance = Malayalam()
        elif language == 'hi_IN':
            instance = Hindi()
        elif language == 'pa_IN':
            instance = Punjabi()
        else:
            return "Unknown language"
        return instance.stem(text)


def getInstance():
    return Stemmer()
