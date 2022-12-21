docker container stop drf_task
docker container rm drf_task
docker image rm drf_task
docker build -t drf_task --progress=plain .
docker run --name drf_task -it -p 8000:8000 drf_task
