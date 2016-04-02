#! /usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from indicstemmer import getInstance


class TestIndicStemmer(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_stemmer(self):
        self.assertEqual(
            u"തുറക്കുക", self.instance.stem(
                u"തുറക്കുന്ന", "ml_IN")[u"തുറക്കുന്ന"])
        self.assertEqual(
            u"खा", self.instance.stem(
                "खाएंगे", "hi_IN")[u"खाएंगे"])
        self.assertEqual(
            u"खेल", self.instance.stem(
                "खेलेंगे", "hi_IN")[u"खेलेंगे"])
        self.assertEqual(
            u"समझ", self.instance.stem(
                "समझाएँ", "hi_IN")[u"समझाएँ"])


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIndicStemmer)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
