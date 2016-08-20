.. indicstemmer documentation master file, created by
   sphinx-quickstart on Tue Sep 17 22:58:08 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to LibIndic Stemmer's documentation!
============================================


LibIndic's stemmer module may be used to extract stems of the words in a
sentence. It is implemented in a rule-based model and follows iterative suffix
stripping to handle multiple levels of inflection. Right now, it supports
Malayalam language only.

Usage
-----


 >>> from libindic.stemmer import Malayalam as mlstemmer
 >>> stemmer = mlstemmer()
 >>> result = stemmer.stem('രാമന്റെ വീട്ടിലേക്ക്')
 >>> for word, stem in result.items():
 ...     print word, " : ", stem
 ... 
 രാമന്റെ  :  രാമൻ
 വീട്ടിലേക്ക്  :  വീട്

API reference
-------------

.. automodule:: stemmer.Malayalam
   :members:
.. automodule:: stemmer.Hindi
   :members:
.. automodule:: stemmer.Punjabi
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

