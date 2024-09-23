docker build -t square:latest -f ./Dockerfile-prod .
docker tag square:latest daccong753.azurecr.io/square:latest
docker push daccong753.azurecr.io/square:latest