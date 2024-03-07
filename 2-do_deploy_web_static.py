#!/usr/bin/python3
'''
    distributes an archive to your web servers
'''
from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['100.25.129.74', '54.144.138.68']


def do_deploy(archive_path):
    '''
        deploys it
    '''
    if not os.path.exists(archive_path):
        return False

    the_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = the_path + name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest))
        return True
    except Exception:
        return False
