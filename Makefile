PYPI_PASS = $(shell cat .pypi_password.txt)

pytest:
	pytest test.py -v 

push_to_pypi:
	rm -fr dist
	python3 -m build
	twine upload -r pypi dist/* --user rouskinlab -p $(PYPI_PASS)
	rm -fr dist
