.PHONY: dev
dev:
	git config --local commit.template .gitmessage
	pipenv install --dev
	pipenv run pip3 install -r requirements-black.txt
