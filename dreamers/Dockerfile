FROM python:3.6-slim

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

CMD python solver.py