# Run local
1. Apply init data
python manage.py loaddata countries.json 
2. Run server 
python manage.py runserver
# Run docker
1. Inside movies_api folder build image
docker build -t movies_api .
2. Run container with volume 
docker run -dp 8000:8000 -v /root/movies_api:./movies_api --name movies_api movies_api