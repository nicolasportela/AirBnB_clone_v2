#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
if [[ $(dpkg -s nginx 2>/dev/null | grep -c "ok installed") -eq 0 ]]
then
    sudo apt-get -y update
    sudo apt-get -y upgrade
    sudo apt-get -y install nginx
fi
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Testing" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R "ubuntu:ubuntu" /data/
new_string="\\\n\tlocation /hbnb_static {\n\t\t alias /data/web_static/current/;\n\t}\n"

check_exist=$(grep "hbnb_static" /etc/nginx/sites-available/default)
if [[ -z $check_exist ]]
then
    sed -i "/server_name _/a $new_string" /etc/nginx/sites-available/default
fi
sudo service nginx restart
