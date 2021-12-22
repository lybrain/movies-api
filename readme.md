# inside movies_api folder build image
docker build -t movies_api .
# run container with volume 
docker run -dp 8000:8000 -v /root/movies_api:./movies_api --name movies_api movies_api