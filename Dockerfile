FROM python:3.12
WORKDIR /code
# Copy only useful, non sensitive info
COPY app/ .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_APP=app
ENV PYTHONPATH=/code
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
# Run as non default user - security
RUN useradd -u 8877 produser
USER produser
CMD ["flask","--app","app/apidbgen", "run","--port","5000"]
