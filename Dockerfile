FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/c_b

COPY ./req.txt /url/src/req.txt
RUN pip install -r /url/src/req.txt


COPY . /usr/src/c_b


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]