.install-deps: requirements.txt
	@pip install -U -r requirements.txt

.develop:
	@pip install -e .

test: .develop
	@py.test -q ./tests

vtest: .develop
	@py.test -s -v ./tests