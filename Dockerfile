FROM python:3.9

# creates directory
WORKDIR /movies_api 

# copy all files with name Pipfile to docker /movies_api/ 
COPY Pipfile* /movies_api/ 

# install pipenv and all dependencies

# Remove cache for pip => "--no-cache-dir" and => "--clear" for pipenv

# install dependencies on system because docker not need for virtual env => --system

# lockfile - declares all dependencies(and sub-dependencies)
# --deploy - raise error if your lockfile is not in sync with pipfile
# by default it will re-lock and re-install
# P.S. only works if you already have a lockfile -- 
RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear 

# copy all files from local folder to docker /movies_api/ 
COPY . /movies_api/ 
# apply migrations

# listen to port 8000
EXPOSE 8000 
CMD python manage.py makemigrations ; python manage.py migrate ; python manage.py runserver 0.0.0.0:8000