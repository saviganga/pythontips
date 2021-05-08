FROM python:3.8

ENV PYTHONUNBUFFERED 1

#create a home directory inside the container 
RUN mkdir /app

#set home directory as working directory
WORKDIR /app

#copy local directory to container directory
COPY . /app

#install all app packages from requirements.txt
RUN pip3 install -r requirements.txt