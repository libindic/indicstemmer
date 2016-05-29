#!/usr/bin/env
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'stemmer'
copyright = '2016, Balasankar C and Santhosh Thottingal'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'libindicstemmerdoc'
latex_elements = {
}
latex_documents = [
    ('index', 'libindicstemmer.tex', 'LibIndic Stemmer Documentation',
     'Balasankar C and Santhosh Thottingal', 'manual'),
]
man_pages = [
    ('index', 'indicstemmer', 'indicstemmer Documentation',
     ['Balasankar C', 'Santhosh Thottingal'], 1)
]
texinfo_documents = [
    ('index', 'indicstemmer', 'indicstemmer Documentation',
     'Balasankar C and Santhosh Thottingal', 'indicstemmer',
     'One line description of project.', 'Miscellaneous'),
]
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'kr'
