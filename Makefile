travis:
	python setup.py test --coverage \
		--coverage-package-name=stemmer
	flake8 --max-complexity 10 --ignore F401 libindic/stemmer

clean:
	find . -iname "*.pyc" -exec rm -vf {} \;
	find . -iname "__pycache__" -delete
	sudo rm -rf build dist *egg* .tox .coverage
