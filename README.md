# LibIndic Stemmer


[![Build Status](https://travis-ci.org/libindic/indicstemmer.svg?branch=master)](https://travis-ci.org/libindic/indicstemmer)
[![Coverage Status](https://coveralls.io/repos/github/libindic/indicstemmer/badge.svg?branch=master)](https://coveralls.io/github/libindic/indicstemmer?branch=master)


LibIndic's stemmer module may be used to extract stems of the words in a
sentence. It is implemented in a rule-based model and follows iterative suffix
stripping to handle multiple levels of inflection. Right now, it supports
Malayalam language only.

## Installation
1. Clone the repository `git clone https://github.com/libindic/indicstemmer.git`
2. Change to the cloned directory `cd indicstemmer`
3. Run setup.py to create installable source `python setup.py sdist`
3. Install using pip `pip install dist/stemmer*.tar.gz`

Note: Prefer using virtualenv for installation as the library is in experimental stage

## Usage

`Input`: String \<str> containing words word1 word2 word3 ...  
`Output`: Dict \<dict> of the format {'word1': 'stem1', 'word2': 'stem2' ... }
```
>>> from libindic.stemmer import Malayalam as mlstemmer
>>> stemmer = mlstemmer()
>>> result = stemmer.stem('രാമന്റെ വീട്ടിലേക്ക്')
>>> for word, stem in result.items():
...     print word, " : ", stem
... 
രാമന്റെ  :  രാമൻ
വീട്ടിലേക്ക്  :  വീട്
```

For more details read the [docs](http://indicstemmer.rtfd.org/)
