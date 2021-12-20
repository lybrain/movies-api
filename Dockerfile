FROM python:3.9

WORKDIR /movies_api # creates directory

COPY Pipfile* ./ # copy all files with name Pipfile to docker ./

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear # install pipenv and all dependencies

COPY . ./ # copy all files from local folder to docker ./
EXPOSE 8000 # listen to port 8000
CMD python manage.py runserver 0.0.0.0:8000