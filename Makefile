travis:
	nosetests -s --with-coverage --cover-package=indicstemmer
	flake8 indicstemmer

clean:
	find . -name "*.pyc" -exec rm -vf {} \;
	find -name __pycache__ -delete

tox:
	tox

flake:
	flake8 silpa tests
