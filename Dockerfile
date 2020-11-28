FROM python:3.8.3-alpine

# env variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system packages required by Wagtail and Django.
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /usr/src/app

# copy project
COPY . .

RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
