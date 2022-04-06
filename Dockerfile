# pull official base image
FROM python:3.10

ENV ENVIRONMENT=dev
ENV TESTING=0

# set working directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV MONGODB_URL="mongodb+srv://autolify_client:ZS3mA0U4kxqkxrqn@auotlify-cluster.3f6lo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# install dependencies
COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app /code/app

# execute uvicorn server
CMD ["uvicorn", "app.main:app", "--reload", "--workers", "2", "--host", "0.0.0.0", "--port", "8080"]