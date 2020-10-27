

FROM python:3.6

MAINTAINER dimensionco@gmail.com

# Expose runserver port
EXPOSE 80

# Copy app content
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install -e .

CMD [ "python", "./manage.py", "runserver", "--host", "0.0.0.0", "--port", "80" ]
