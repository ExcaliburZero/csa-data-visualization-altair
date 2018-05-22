build:
	pipenv run python -m csadatavis

typecheck:
	pipenv run mypy csadatavis --ignore-missing-imports --disallow-untyped-defs

test:
	pipenv run nosetests --with-coverage --cover-package=csadatavis --cover-html

download_data:
	mkdir -p data
	curl -o data/meetings.csv http://www.cs.oswego.edu/~cwells2/code/csa-data-visualization/meetings.csv
