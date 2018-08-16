FROM python:3.5.2
WORKDIR /sever
COPY ./server.py .
CMD python3 ./server.py
