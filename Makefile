.PHONY: dev
dev:
	git config --local commit.template .gitmessage
	pipenv install --dev
