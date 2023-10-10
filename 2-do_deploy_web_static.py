#!/usr/bin/python3
from fabric.api import run, env, put
from os.path import exists
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
"""

env.hosts = ['100.26.164.241', '34.229.49.155']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """ Deploy archive to web-servers """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_file = archive_path.split('/')[-1]
        archive_folder = archive_file.split('.')[0]
        release_folder = '/data/web_static/releases/{}'.format(archive_folder)

        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_file, release_folder))
        run('rm /tmp/{}'.format(archive_file))
        run('mv {}/web_static/* {}'.format(release_folder, release_folder))
        run('rm -rf /data/web_static/current')
        run('rm -rf {}/web_static'.format(release_folder))
        run('ln -s {}/ /data/web_static/current'.format(release_folder))
    except Exception:
        return False
    else:
        return True
