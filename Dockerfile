# pull the official base image.
FROM python:3.8.3-alpine

# set work directory.
WORKDIR /usr/src/app

# set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project.
COPY . /usr/src/app

# install dependencies.
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# expose application on port 8000.
EXPOSE 8000

# entry command.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

