pytest:
	pytest test.py -v 

push_to_pypi:
	rm -fr dist
	python3 -m build
	twine upload -r pypi dist/* --user rouskinlab --password cat .pypi_password
	rm -fr dist
