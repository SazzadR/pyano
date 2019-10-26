#!/bin/bash

function log() {
    echo -e "\e[1;42m$1\e[0m"
}

sudo apt-get -y update
sudo apt-get -y install openjdk-8-jdk
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo add-apt-repository "deb https://pkg.jenkins.io/debian-stable binary/"
sudo apt-get -y update
sudo apt-get -y install jenkins
sudo /etc/init.d/jenkins stop
sudo /etc/init.d/jenkins start --httpListenAddress=0.0.0.0 --httpPort=8080
