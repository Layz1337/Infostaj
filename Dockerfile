FROM python:3.5.2
WORKDIR /sever
COPY . .
CMD python3 ./server.py
