FROM library/python:3.7-alpine as base
FROM base as builder

RUN mkdir /install

WORKDIR /install



ENV LIBRARY_PATH=/lib:/usr/lib

COPY requirements.txt /requirements.txt

RUN python -m pip install --install-option="--prefix=/install" -r /requirements.txt



FROM base

COPY --from=builder /install /usr/local

RUN apk --no-cache --quiet add libpq

ENV PROJECT_PATH=/usr/src/app

RUN echo "Installing into $PROJECT_PATH..."

RUN mkdir -p $PROJECT_PATH

RUN mkdir -p $PROJECT_PATH/media
RUN mkdir -p $PROJECT_PATH/static/assets

# We need a .env file to start the server.
#COPY deploy/.env.captain $PROJECT_PATH/.env
RUN touch $PROJECT_PATH/.env

# Run all commands in this new directory.
WORKDIR $PROJECT_PATH

# Copy this directory to the image.
COPY . $PROJECT_PATH

# Open port 80 to traffic.
EXPOSE 8080

# Run a startup script in the specified directory.
CMD ["python", "manage.py", "runserver"]
