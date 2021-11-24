# Test My microservice
# Linux x64
FROM ubuntu:latest

# Create a new dicrectory named myservice in the #ubuntu:latest docker filesystem and copy the mymicroservices #contents from windows10 machine

COPY . /mymicroservice

WORKDIR /mymicroservice

ENV VIRTUAL_ENV=/mymicroservice/venv

# Install virtual environment
RUN apt-get update -y \
    && apt install python3 -y \
    && apt install python3-pip -y \
    && apt install python3-venv -y \
    && python3 -m venv $VIRTUAL_ENV
 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"   
RUN pip install flask
RUN pip install configobj

EXPOSE 5000

#ENTRYPOINT ["/mymicroservice/venv/bin/python3", "/mymicroservice/run.py"]
