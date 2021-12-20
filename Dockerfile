FROM python:3.9

# creates directory
WORKDIR /movies_api 

# copy all files with name Pipfile to docker ./
COPY Pipfile* ./ 

# install pipenv and all dependencies
RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear 

# copy all files from local folder to docker ./
COPY . ./ 

# listen to port 8000
EXPOSE 8000 
CMD "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"