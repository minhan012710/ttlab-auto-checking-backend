### Install amd64 emulator
# docker run --privileged --rm tonistiigi/binfmt --install amd64 

### Build docker image
# docker buildx build --platform=linux/amd64 -t tims-ai .

### Run docker container
# docker run --platform=linux/amd64 -p 9000:9000 --name=tims-ai tims-ai

# pull docker image
FROM python:3.9

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./ems-checking/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# copy project
COPY . .
