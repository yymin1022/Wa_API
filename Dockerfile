FROM ubuntu:20.04

WORKDIR /app
ADD ./ /app

RUN apt update -y
RUN apt install apache2 libapache2-mod-wsgi-py3 python3 python3-flask python3-pip -y
RUN python3 -m pip install -r requirements.txt
RUN dd if=/app/apache2script_docker of=/etc/apache2/sites-available/000-default.conf

CMD ["/etc/init.d/apacge2", "start"]