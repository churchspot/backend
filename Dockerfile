FROM python:3.8.0

COPY . /churchspot

WORKDIR /churchspot

RUN pip install -r requirements.txt

ENV FLASK_APP=backend
CMD flask run --host=0.0.0.0
