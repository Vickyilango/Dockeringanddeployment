FROM python:3

WORKDIR /app
# Make which ever folder you want to start your main function in here. I am giving /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD [ "uwsgi", "app.ini" ]
