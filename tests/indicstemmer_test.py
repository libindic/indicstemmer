#! /usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from indicstemmer import getInstance


class TestIndicStemmer(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_stemmer(self):
        self.assertEqual(u"തുറക്കുക",self.instance.stem(u"തുറക്കുന്ന")[u"തുറക്കുന്ന"])

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIndicStemmer)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
