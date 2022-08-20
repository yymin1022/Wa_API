FROM ubuntu:20.04

WORKDIR /app
ADD ./ /app

ENV DEBIAN_FRONTEND=noninteractive

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["python3 /app/main.py"]