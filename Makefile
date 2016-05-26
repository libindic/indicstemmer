travis:
	nosetests -s --with-coverage --cover-package=libindic

clean:
	find . -name "*.pyc" -exec rm -vf {} \;
	find -name __pycache__ -delete

tox:
	tox
