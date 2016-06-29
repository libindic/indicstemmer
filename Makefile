travis:
	python setup.py test --coverage \
		--coverage-package-name=libindic.stemmer
	flake8 --max-complexity 10 libindic/stemmer
	python setup.py test --coverage \
		--coverage-package-name=libindic.inflector
	flake8 --max-complexity 10 libindic/inflector

clean:
	find . -iname "*.pyc" -exec rm -vf {} \;
	find . -iname "__pycache__" -delete
	sudo rm -rf build dist *egg* .tox .coverage
