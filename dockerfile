FROM python:3

MAINTAINER dimensionco@gmail.com

WORKDIR /usr/src/app

COPY Python-master ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY . .
run pwd 
EXPOSE 80


#CMD [ "python3", "./Python-master/manage.py runserver --host 0.0.0.0 --port 80" ]
#CMD [ "python3", "manage.py runserver --host 0.0.0.0 --port 80" ]
CMD [ "python ./manage.py runserver --host 0.0.0.0 --port 80" ]