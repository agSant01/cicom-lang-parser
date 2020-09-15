IN?=./tests/test_files/test1.txt

init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python -m project -i $(IN)

lexer:
	python project/lexer.py -i $(IN)

.PHONY: init test