# inside movies_api folder build image
docker build -t movies_api .
# build container
docker run -dp 8000:8000 movies_api