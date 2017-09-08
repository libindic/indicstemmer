#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from testtools import TestCase

from ..Malayalam import Malayalam
from .. import Stemmer
from ..inflector import Inflector as inflector


class MalayalamInflectorTest(TestCase):

    def setUp(self):
        super(MalayalamInflectorTest, self).setUp()
        self.stemmer = Stemmer()
        self.malayalam = Malayalam()
        self.inflector = inflector(lang='ml')
        test_path = os.path.abspath(
            os.path.join(__file__, '../test_words.txt'))
        test_file = codecs.open(test_path, encoding="utf-8")
        words_raw = test_file.readlines()
        self.words = [x.strip() for x in words_raw]

    def test_inflect(self):
        '''
        Test whether inflection returns original word when used with the output
        of stemmer.
        '''
        for word in self.words:
            root_word = self.malayalam.singleencode(word)
            stem_result = self.stemmer.stem("malayalam", root_word)[root_word]
            stem = stem_result['stem']
            tag_list = stem_result['inflection']
            inflection_result = self.inflector.inflect(stem, tag_list)
            inflection_result = self.malayalam.singleencode(inflection_result)
            assert root_word == inflection_result
