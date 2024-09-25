docker build -t square:latest -f ./Dockerfile-prod .
docker tag square:latest daccongsit753.azurecr.io/square:latest
docker push daccongsit753.azurecr.io/square:latest