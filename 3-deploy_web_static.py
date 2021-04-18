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
    name = "web_static_" + datetime.strftime(datetime.now(),
                                             "%Y%m%d%H%M%S") + ".tgz"
    try:
        local("tar -czvf ./versions/{} ./web_static" .format(name))
        return(name)
    except:
        return(None)


def do_deploy(archive_path):
    """function to distribute an archive to web server"""
    if not (path.exists(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        """ file_name name of file with .tgz """
        file_name = archive_path.split("/")[1]
        """ file_name2 name of file without .tgz """
        file_name2 = file_name.split(".")[0]
        """ final_name name of path of directory """
        final_name = "/data/web_static/releases/" + file_name2 + "/"
        run("mkdir -p " + final_name)
        run("tar -xzf /tmp/" + file_name + " -C " + final_name)
        run("rm /tmp/" + file_name)
        run("mv " + final_name + "web_static/* " + final_name)
        run("rm -rf " + final_name + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + final_name + " /data/web_static/current")
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
