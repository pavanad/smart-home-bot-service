.PHONY: help clean lint run

.DEFAULT: help

help:
	@echo "\nUsage:"
	@echo "make <command>"
	@echo "\nAvailable Commands:"
	@echo "- clean\t\t Run clean project"
	@echo "- lint\t\t Check python code against some of the style conventions in PEP 8"
	@echo "- run\t\t Run Bot Service\n\n"

clean:
	@echo "\n> Cleaning project\n";\
	find . -name '*.pyc' -exec rm --force {} +;\
	find . -name '*.pyo' -exec rm --force {} +;\
	find . | grep -E "__pycache__|.pyc" | xargs rm -rf;\

lint:
	@echo "\n> Check python code PEP 8\n";\
	black . & flake8 . & bandit -r -lll .;\

run:
	@echo "\n> Run Bot Service\n";\
	python app/