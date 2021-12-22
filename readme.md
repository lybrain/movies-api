# Run local
<p>1. Apply init data</p>
<p>python manage.py loaddata countries.json </p>
<p>2. Run server </p>
<p>python manage.py runserver</p>
<h1>Run docker</h1>
<p>1. Inside movies_api folder build image</p>
<p>docker build -t movies_api .</p>
<p>2. Run container with volume </p>
<p>docker run -dp 8000:8000 -v /root/movies_api:./movies_api --name movies_api movies_api</p>