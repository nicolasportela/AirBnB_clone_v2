#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
if [[ $(dpkg -s nginx 2>/dev/null | grep -c "ok installed") -eq 0 ]]
then
    sudo apt-get -y update
    sudo apt-get -y upgrade
    sudo apt-get -y install nginx
fi
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# nice conditional
# if [[ -e "/data/web_static/current" ]]
# then
#	  rm /data/web_static/current
# fi
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "48i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
# alternative:
# if [[ -z $check_exist ]]
# then
# sed -i "/server_name _/a $new_string" /etc/nginx/sites-available/default
# fi
sudo service nginx restart
