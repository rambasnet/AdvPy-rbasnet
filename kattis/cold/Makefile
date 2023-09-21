PROGRAM = python3
MAIN = cold.py

all: type style unittest localtest clean submit

localtest:
	@cat 1.in | $(PROGRAM) $(MAIN) | diff - 1.ans
	@cat 2.in | $(PROGRAM) $(MAIN) | diff - 2.ans
	@echo "all test done..."

unittest:
	pytest

run:
	$(PROGRAM) $(MAIN)
	
type:
	mypy --strict $(MAIN)
	mypy --strict test_main.py

style:
	flake8 $(MAIN)
	flake8 test_main.py

clean:
	@rm -rf __pycache__
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@echo "All cleaned."

submit:
	kattis -f $(MAIN)
