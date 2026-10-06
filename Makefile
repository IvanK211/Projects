PYTHON ?= python3

.PHONY: check test demo index
check:
	$(PYTHON) tools/privacy_scan.py
	$(PYTHON) tools/check_repository.py
test:
	$(PYTHON) -m unittest discover -s tests -v
demo:
	$(PYTHON) tools/run_demo.py
index:
	$(PYTHON) tools/build_index.py
