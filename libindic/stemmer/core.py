#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .Malayalam import Malayalam
from .Hindi import Hindi
from .Punjabi import Punjabi


class Stemmer:

    def stem(self, language, text):
        if language.lower() == 'malayalam':
            instance = Malayalam()
        elif language.lower() == 'hindi':
            instance = Hindi()
        elif language.lower() == 'punjabi':
            instance = Punjabi
        else:
            return "Unknown language"
        return instance.stem(text)


def getInstance():
    return Stemmer()
