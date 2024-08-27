FROM python:3.10.6

ENV PYTHONHTTPSVERIFY 0
ENV TZ Asia/Seoul

WORKDIR /app
ADD ./ /app

RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install --upgrade certifi

EXPOSE 80

ENTRYPOINT ["python3", "/app/main.py"]
