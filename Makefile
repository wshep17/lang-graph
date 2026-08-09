ROOT := $(abspath .)
PYTHON := $(ROOT)/.venv/bin/python

.PHONY: help

help:
	@echo "Usage: make <name>-agent"
	@echo ""
	@echo "Examples:"
	@echo "  make calculator-agent"
	@echo "  make hello-world-agent"
	@echo ""
	@echo "Available agent dirs:"
	@ls -1 agents

# make calculator-agent     -> agents/calculator/calculator-agent.py
# make hello-world-agent    -> agents/hello-world-agent/hello-world-agent.py
%-agent:
	@set -e; \
	name="$*"; \
	entry="$$name-agent.py"; \
	if [ -d "agents/$$name" ]; then \
		dir="agents/$$name"; \
	elif [ -d "agents/$$name-agent" ]; then \
		dir="agents/$$name-agent"; \
	else \
		echo "error: no agents/$$name or agents/$$name-agent"; \
		exit 1; \
	fi; \
	if [ ! -f "$$dir/$$entry" ]; then \
		echo "error: missing $$dir/$$entry"; \
		exit 1; \
	fi; \
	echo "→ $$dir/$$entry"; \
	cd "$$dir" && $(PYTHON) "$$entry"
