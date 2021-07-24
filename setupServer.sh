#!/bin/bash

echo "Installing Requiered Packages"
sudo apt install apache2 libapache2-mod-wsgi-py3 python3 python3-flask python3-pip -y

while:
do
    echo "Please input Port Number for WA API Server"
    read serverPort
done

if [ $serverPort = "80" ]
then
    sudo cat apache2script > /etc/apache2/sites-available/000-default.conf
else
    sudo cat apache2script >> /etc/apache2/sites-available/000-default.conf
    sudo echo Listen $serverPort >> /etc/apache2/ports.conf
fi

curDirectory=$(pwd)

sudo sed -i 's|varDirectory|$curDirectory|g' /etc/apache2/sites-available/000-default.conf

echo "Setup Done..!"

echo "Start API Server from now? (y/n)"

read doStart

if [$doStart = "y"]
then
    sudo /etc/init.d/apache2 start
else
    echo "You can start API Server with this command : /etc/init.d/apache2 start"
fi
