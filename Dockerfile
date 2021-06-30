# Base Image
FROM python:3.8

# create and set working directory
RUN mkdir /opt/project
WORKDIR /opt/project

# Install system dependencies
RUN apt-get update

# install dependencies
COPY src/ ./
COPY commands/ ./
COPY ./requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

CMD ["bash"]
