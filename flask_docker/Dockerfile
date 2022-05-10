FROM python:3.8-alpine

RUN mkdir pucsd

COPY . /pucsd

WORKDIR /pucsd

RUN pip install Flask

EXPOSE 5000

ENTRYPOINT [ "python", "run.py"]

