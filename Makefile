# default variables
DEFAULT_OUT_DIR=./out/
DEFAULT_TEST_DIR=./tests/test_files/
DEFAULT_TEST_FILE=prof-test.txt
DEFAULT_TEST_OUT_DIR=$(DEFAULT_OUT_DIR)test_results/
DEFAULT_EXPECTED_DIR=./tests/expected_out/

MODE=parser

IN?=$(DEFAULT_TEST_DIR)$(DEFAULT_TEST_FILE)
OUT?=$(DEFAULT_TEST_OUT_DIR)$(notdir $(basename $(IN))).$(MODE).out
EXPECTED=$(DEFAULT_EXPECTED_DIR)$(notdir $(basename $(IN))).$(MODE).expected

init:
	mkdir -p $(DEFAULT_OUT_DIR) $(DEFAULT_TEST_OUT_DIR)
	pip install -r requirements.txt

lex:
	@ $(eval MODE=lexer)
	python project/lexer.py -i $(IN) > $(OUT)
	@ less $(OUT)

test-lex: lex
	@ (diff $(OUT) $(EXPECTED) && \
	  	echo "\033[33m[INFO] Input file: $(IN)" && \
	  	echo "[INFO] Output file: $(OUT)\033[0m" && \
	  	echo "\033[92m\033[1m[SUCCESS] Test OK!\033[0m" ) || \
	  (echo "\033[91m\033[1m[ERROR] Test FAILED\033[0m")

parse:
	@ $(eval MODE=parser)
	python -m project -i $(IN)

test-parse:
	@ $(eval MODE=parser)
	@ # 2> stderr to $(OUT) ; 1> stdout to null (discard)
	python -m project -d -i $(IN) 2> $(OUT) 1> /dev/null
	@ (diff $(OUT) $(EXPECTED) && \
	  	echo "\033[33m[INFO] Input file: $(IN)" && \
	  	echo "\033[33m[INFO] Output file: $(OUT)\033[0m" && \
	  	echo "\033[92m\033[1m[SUCCESS] Test OK!\033[0m" ) || \
	  (echo "\033[91m\033[1m[ERROR] Test FAILED\033[0m")

test: test-lex test-parse


.PHONY: init test-parse