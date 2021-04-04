FROM alpine:2.7
RUN mkdir -p /opt/djangoSIGE/
WORKDIR /opt/djangoSIGE/
COPY requirements.txt /opt/djangoSIGE/
RUN apk add --no-cache python python-dev \
    && pip install -r requirements.txt 

EXPOSE 80

