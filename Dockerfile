FROM python:3.7

RUN mkdir /app
WORKDIR /app

ADD . /app/

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

ENV PORT=8000

RUN pip install -r requirements.txt

EXPOSE 8000

# Run a startup script in the specified directory.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
