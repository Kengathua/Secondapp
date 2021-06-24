# Readme
## Django REST API implementation 
### Display amazon products

**This project aims at achieving a RESTful backend implementation of a small e-shop site. I aim at scraping the amazon site to obtain the products, their categories and the sellers. The values will then be stored in a database which will then be queried by the API.**

_I am yet to understand how to use routers for my urls_

It has:

1. Products
   * id
   * image
   * asin
   * seller
   * price
   * name
   * category
2. Categories 
   * id
   * title
   * image

3. Sellers
   * id
   * name


I also made an attempt to make a docker container for it as follows 

Dockerfile

```
FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY .requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
     
```

docker-compose.yml

```
version: '3'

services: 
    web:
        build: .
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
            - .:/code
        ports: 
            - "8000:8000"
```

requiremnts.txt

```
Django==3.2
gunicorn==20.1.0
     
```
