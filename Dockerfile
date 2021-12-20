FROM python:3.9

# creates directory
WORKDIR /movies_api 

# copy all files with name Pipfile to docker ./
COPY Pipfile* ./ 

# install pipenv and all dependencies

# You won't have any unnecessary cache files left over using => --no-cache-dir option for pip 
# and => --clear option for pipenv

# install dependencies on system because docker not need for virtual env => --system

# --deploy only works if you already have a lockfile -- 
# by default pipenv will compare your lockfile to your pipfile 
# (in both cases, assuming you have one), and if your lockfile is not in sync, 
# it will re-lock and re-install. When you pass the --deploy flag, 
# pipenv will instead fail with an error and let you know that 
# things are out of sync, rather than implicitly installing the new things. 
RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear 

# copy all files from local folder to docker ./
COPY . ./ 
# apply migrations
RUN python manage.py migrate 

# listen to port 8000
EXPOSE 8000 
CMD python manage.py makemigrations ; python manage.py migrate ; python manage.py runserver 0.0.0.0:8000