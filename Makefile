.PHONY: install
install:
	poetry install --no-dev

.PHONY: install-dev
install-dev:
	poetry install

.PHONY: lint
lint:
	poetry run flake8 cdk/ lambda/
	poetry run isort --check-only --profile black cdk/ lambda/
	poetry run black --check --diff cdk/ lambda/

.PHONY: fmt format
fmt: format
format:
	poetry run isort --profile black cdk/ lambda/
	poetry run black cdk/ lambda/

.PHONY: diff
diff:
	poetry run dotenv run npx cdk diff --app cdk/app.py || true

.PHONY: deploy
deploy:
	poetry run dotenv run npx cdk deploy --app cdk/app.py --require-approval never

.PHONY: destroy
destroy:
	poetry run dotenv run npx cdk destroy --app cdk/app.py --force
