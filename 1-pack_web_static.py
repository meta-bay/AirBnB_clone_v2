#!/usr/bin/python3
'''
    Compress before sending
'''
from datetime import datetime
from fabric.api import local


def do_pack():
    '''
        generates a .tgz archive
    '''
    try:
        local("mkdir -p versions")
        res = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.now().strftime("%Y%m%d%H%M%S")),
                    capture=True)
        return res
    except Exception:
        return None
