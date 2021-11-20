#!/bin/bash

echo "Installing Requiered Dependecies/Packages..."
echo ""
sudo apt install apache2 libapache2-mod-wsgi-py3 python3 python3-flask python3-pip -y

echo "Enabling Apache2 WSGI Module..."
sudo a2enmod wsgi
echo ""

echo "Installing Python3 Required Dependencies/Modules with PIP"
python3 -m pip install flask requests xmltodict
echo ""

echo
echo "Please input Port Number for WA API Server"
read serverPort
echo ""

if [ $serverPort = "80" ]
then
    sudo cat apache2script > /etc/apache2/sites-available/000-default.conf
else
    sudo cat apache2script >> /etc/apache2/sites-available/000-default.conf
    sudo echo Listen $serverPort >> /etc/apache2/ports.conf
fi

curDirectory=$(pwd)

sudo sed -i "s|varDirectory|$curDirectory|g" $curDirectory/flask_app.wsgi
sudo sed -i "s|varDirectory|$curDirectory|g" /etc/apache2/sites-available/000-default.conf
sudo sed -i "s|varPort|$serverPort|g" /etc/apache2/sites-available/000-default.conf
echo ""

echo "Setup Done..!"
echo ""

echo "Start API Server from now? (y/n)"

read doStart
echo ""

if [ $doStart = "y" ]
then
    sudo /etc/init.d/apache2 start
else
    echo "You can start API Server manually with this command : /etc/init.d/apache2 start"
    echo ""
fi
