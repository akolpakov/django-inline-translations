# This file is part of django-inline-translations.
# https://github.com/akolpakov/django-inline-translations

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Andrey Kolpakov <aakolpakov@gmail.com>

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install all dependencies (do not forget to create a virtualenv first)
setup:
	@pip install -U -e .\[tests\]

# test your application (tests in the tests/ directory)
test: unit

unit:
	@coverage run ./tests/runtests.py -vv --with-yanc
	@coverage report -m --fail-under=80

# show coverage in html format
coverage-html: unit
	@coverage html

test_no_coverage:
	python ./tests/runtests.py

# run tests against all supported python versions
tox:
	@tox

register:
	@python setup.py sdist register

upload:
	@python setup.py sdist upload
