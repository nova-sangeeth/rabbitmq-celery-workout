echo "Building The rabbitmq container...."
docker build --pull --rm -f "Dockerfile" -t root:latest "."