#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import run, put, env
from os.path import exists

env.hosts = ['100.26.164.241', '34.229.49.155']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        archive_filename = archive_path.split("/")[-1]
        folder_name = archive_filename.split(".")[0]
        release_path = "/data/web_static/releases/{}/".format(folder_name)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

        run("rm /tmp/{}".format(archive_filename))

        run("rm -f /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        return True

    except Exception:
        return False
