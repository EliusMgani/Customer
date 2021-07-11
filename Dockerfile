FROM python:3.9.6-slim-buster

WORKDIR /home/dev2/workspace

RUN pip install --upgrade pip

COPY /requirements.txt /home/dev2/workspace

RUN pip install -r requirements.txt

COPY . /home/dev2/workspace

EXPOSE 8003

CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]