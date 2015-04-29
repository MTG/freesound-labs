"""
Deploy freesound labs index to labs.freesound.org
"""


from __future__ import with_statement
from fabric.api import *
from fabric.contrib.files import put

env.hosts = ['ffont@fs-labs.s.upf.edu']
remote_dir = '/homedtic/ffont/test/freesound-labs/'

def __copy_files():
    # Copia l'arxiu de local_settings.py al lloc corresponent
    with cd(remote_dir):
        put("_site", remote_dir)

def __pull():
    # Pull del repo de git
    with cd(remote_dir):
        run("git pull")

def __build():
    # Build static site
    with cd(remote_dir):
        run("jekyll build")

def deploy_from_local_site():
    __copy_files()

def deploy():
	__pull()
	__build()