.PHONY: reset update

reset:
	git reset --hard origin/master

update: reset
	git remote update
	git pull origin master

