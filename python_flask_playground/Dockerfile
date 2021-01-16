FROM python:3.8.0-slim

# Set install location 
RUN mkdir /var/opt/python_flask_playground
WORKDIR /var/opt/python_flask_playground

# Copy source code
COPY vehicle_api /var/opt/python_flask_playground

RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && apt-get update \
 && apt-get install gcc -y \
 && apt-get upgrade -y \
 && apt-get install -y uwsgi-plugin-python3 python3-pip \
 uwsgi-plugin-python3 \
 curl \
 && pip3 install --upgrade pip

# Install python requirements
RUN pip3 install --no-cache-dir -r /var/opt/python_flask_playground/requirements.txt

WORKDIR /var/opt/python_flask_playground

RUN mkdir -p /var/log/uwsgi

ENV FLASK_APP vehicle_api

EXPOSE 8080

CMD ["uwsgi","--ini","/var/opt/python_flask_playground/vehicle_api/uwsgi.ini"]
