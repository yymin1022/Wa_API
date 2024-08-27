FROM ubuntu:20.04

ENV TZ Asia/Seoul

WORKDIR /app
ADD ./ /app

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN python3 -m pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python3", "/app/main.py"]
