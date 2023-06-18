install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203 *.py devopslib

test:
	python -m pytest -vv --cov=devopslib test_*.py

format:
	black *.py devopslib/*.py

post-install:
	python -m textblob.download_corpora

deploy:
	aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 297758011529.dkr.ecr.ap-southeast-1.amazonaws.com
	docker build -t devops-june-2023 .
	docker tag devops-june-2023:latest 297758011529.dkr.ecr.ap-southeast-1.amazonaws.com/devops-june-2023:latest
	docker push 297758011529.dkr.ecr.ap-southeast-1.amazonaws.com/devops-june-2023:latest

all: install post-install format lint test deploy
	