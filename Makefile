.PHONY: build deploy rm test run clean

build:
	docker build -t villagomezimg:1.0.1 .
	
deploy:
	docker stack deploy --with-registry-auth -c stack.yml doraemon

rm:
	docker stack rm doraemon

test:
	pytest test_app.py -v --cov=app

run:
	python app.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache htmlcov .coverage