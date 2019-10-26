#!/bin/bash

function log() {
    echo -e "\e[1;42m$1\e[0m"
}

function install_codedeploy_agent() {
    sudo apt-get -y update
    sudo apt-get install -y ruby
    sudo apt-get install -y wget
    cd /home/ubuntu
    wget https://aws-codedeploy-us-west-2.s3.us-west-2.amazonaws.com/latest/install
    chmod +x ./install
    sudo ./install auto
    sudo service codedeploy-agent stop
    sudo service codedeploy-agent start
}

function install_python() {
    if ! command -v python3.7 &>/dev/null; then
        sudo add-apt-repository -y ppa:deadsnakes/ppa
        sudo apt install -y python3.7
        sudo apt install -y python3-pip
    fi
}

function install_postgresql_client() {
    sudo apt-get -y install postgresql-client
}

function create_database() {
    rds_host=$1
    rds_username=$2
    rds_password=$3

    export PGPASSWORD=$rds_password

    psql -h "$rds_host" -U "$rds_username" -p 5432 -c "
    CREATE DATABASE pizzaluvrs
        WITH OWNER = $rds_username
            ENCODING = 'UTF8'
            LC_COLLATE = 'en_US.UTF-8'
            LC_CTYPE = 'en_US.UTF-8'
            CONNECTION LIMIT = -1;
    "
}

function install_git() {
    sudo apt-get -y remove git
    sudo add-apt-repository -y ppa:git-core/ppa
    sudo apt-get -y update
    sudo apt-get -y install git
}

function clone_project() {
    if [ -d "/home/ubuntu/code/pizzaluvrs" ]; then
        echo "Project exists!"
        exit 0
    else
        rm -rf code
        git clone --depth 1 https://github.com/SazzadR/pyano.git code
        cd code
        git filter-branch --prune-empty --subdirectory-filter aws HEAD
    fi
}

function start_project() {
    cd /home/ubuntu/code/pizzaluvrs

    python3.7 -m pip install -r requirements.txt

    cp .env.example .env
    rds_host=$1
    rds_username=$2
    rds_password=$3
    sed -i -E "s/DB_HOST=.*?/DB_HOST=${rds_host}/g" /home/ubuntu/code/pizzaluvrs/.env
    sed -i -E "s/DB_PORT=.*?/DB_PORT=5432/g" /home/ubuntu/code/pizzaluvrs/.env
    sed -i -E "s/DB_USERNAME=.*?/DB_USERNAME=${rds_username}/g" /home/ubuntu/code/pizzaluvrs/.env
    sed -i -E "s/DB_PASSWORD=.*?/DB_PASSWORD=${rds_password}/g" /home/ubuntu/code/pizzaluvrs/.env
    sed -i -E "s/DB_DATABASE=.*?/DB_DATABASE=pizzaluvrs/g" /home/ubuntu/code/pizzaluvrs/.env
    sed -i -E "s/DB_SCHEMA=.*?/DB_SCHEMA=public/g" /home/ubuntu/code/pizzaluvrs/.env

    python3.7 manage.py migrate
    screen -d -m -S bukkit bash -c "cd /home/ubuntu/code/pizzaluvrs && python3.7 manage.py runserver 0.0.0.0:8000"

    log "puzzaluvrs started successfully...!"
}

install_codedeploy_agent
install_python
install_postgresql_client
create_database "$1" "$2" "$3"
install_git
clone_project
start_project "$1" "$2" "$3"
