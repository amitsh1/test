FROM joyzoursky/python-chromedriver
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
WORKDIR /code
CMD ["sh", "/code/docker-entrypoint.sh"]