FROM python:3.12
WORKDIR dbgen
COPY . dbgen/databasegen
RUN docker run -v dbgenvol:./../dbgenvol -d
RUN docker volume prune
RUN pip install flask
RUN pip install faker
EXPOSE 5000
CMD ["flask","--app","databasegen/apidbgen","--debug","run","--port","5000"]
