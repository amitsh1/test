# build Docker:
docker build -t okapi .

# Tests:
docker run -it -v ${PWD}:/code -p 8000:8000 okapi python manage.py test tests

# run server:
docker run -it -v ${PWD}:/code -p 8000:8000 okapi