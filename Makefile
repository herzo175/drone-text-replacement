NAME=drone-text-replacement
TEST_DIR=tests/test1

build:
	docker build -t $(NAME):latest ./

run:
	docker run --env-file $(TEST_DIR)/.env $(NAME):latest