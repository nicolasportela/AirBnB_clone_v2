#!/usr/bin/python3
"""Fabric script that creates and distributes an archive
to your web servers, using the function deploy"""

from fabric.api import local, put, env, run
from os import path
from datetime import datetime
env.hosts = ['34.74.134.187', '34.74.176.2']
env.user = "ubuntu"


def do_pack():
    """function to compress file"""
    local("mkdir -p versions")
    # create the name of file in str format from datetime.now
    now = datetime.now()
    name = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    try:
        local("tar -czvf versions/{} web_static" .format(name))
        return name
    except:
        return None


def do_deploy(archive_path):
    """function to distribute an archive to web server"""
    if not (path.exists(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        name = archive_path.split('/')[1].split('.')[0]
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
            .format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except:
        return False


def deploy():
    """Full deployment"""
    filepath = do_pack()
    if filepath:
        return do_deploy(filepath)
    else:
        return False
