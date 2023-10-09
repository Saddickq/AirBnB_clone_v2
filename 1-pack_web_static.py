#!/usr/bin/python3
from fabric.api import run, local
from datetime import datetime
"""
fabric
"""


def do_pack():
    """ a Fabric script that generates a .tgz archive from
    the contentsof the web_static folder of your AirBnB
    Clone repo, using the function do_pack. """

    try:
        local('mkdir -p versions/')
        time = datatime.now().strftime('%Y%m%d%H%M%S')
        archive = "versions/web_static_{}.tgz".format(time)
        local('tar -cvzf {} web_static/'.format(archive))
    except Exception:
        return None
    else:
        return archive
