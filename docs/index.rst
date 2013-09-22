.. indicstemmer documentation master file, created by
   sphinx-quickstart on Tue Sep 17 22:58:08 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to indicstemmer's documentation!
========================================

This application helps you to stem the words in the given text.
Currently supports only Malayalam. Note that this is very
experimental and uses a rule based approach.

Usage
-----

 >>> from indicstemer import getInstance
 >>> s = getInstance()
 >>> s.stem(u"ഇടുക്കി: മഴ കുറഞ്ഞ പശ്ചാത്തലത്തില്‍ ഇടുക്കി അണക്കെട്ട് മൂന്ന് ദിവസത്തേക്ക് തുറക്കേണ്ട")
 {u'': u'', u'\u0d26\u0d3f\u0d35\u0d38\u0d24\u0d4d\u0d24\u0d47\u0d15\u0d4d\u0d15\u0d4d': u'\u0d26\u0d3f\u0d35\u0d38\u0d02',
 u'\u0d07\u0d1f\u0d41\u0d15\u0d4d\u0d15\u0d3f': u'\u0d07\u0d1f\u0d41\u0d15\u0d4d\u0d15\u0d41\u0d15',
 u'\u0d15\u0d41\u0d31\u0d1e\u0d4d\u0d1e': u'\u0d15\u0d41\u0d31\u0d1e\u0d4d\u0d1e',
 u'\u0d05\u0d23\u0d15\u0d4d\u0d15\u0d46\u0d1f\u0d4d\u0d1f\u0d4d': u'\u0d05\u0d23\u0d15\u0d4d\u0d15\u0d46\u0d1f\u0d4d\u0d1f\u0d4d',
 u'\u0d2e\u0d42\u0d28\u0d4d\u0d28\u0d4d': u'\u0d2e\u0d42\u0d28\u0d4d\u0d28\u0d4d',
 u'\u0d2a\u0d36\u0d4d\u0d1a\u0d3e\u0d24\u0d4d\u0d24\u0d32\u0d24\u0d4d\u0d24\u0d3f\u0d32\u0d4d\u200d': u'\u0d2a\u0d36\u0d4d\u0d1a\u0d3e\u0d24\u0d4d\u0d24\u0d32\u0d02',
 u'\u0d24\u0d41\u0d31\u0d15\u0d4d\u0d15\u0d47\u0d23\u0d4d\u0d1f': u'\u0d24\u0d41\u0d31\u0d15\u0d4d\u0d15\u0d47\u0d23\u0d4d\u0d1f',
 u'\u0d2e\u0d34': u'\u0d2e\u0d34'}

API reference
-------------

.. automodule:: indicstemmer.core
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

