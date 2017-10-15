from fabric.api import *
from fabric.contrib.files import *
import time

#deploy script for QCLOUD
def production():
    env.hosts=['101.132.146.191']
    env.dj_setting='production'

def deploy():
    #deploy web
    with cd("/mnt/github/leLife/tasks/"):
        run("git pull origin master")
        run("/mnt/envs/env_tasks/bin/pip3 install -r requirements.txt")
    with cd("/mnt/deploy_bak"):
        run("rm -rf tasks")
        run("cp -r /mnt/deploy/worker worker")
    with cd("/mnt/deploy/worker"):
        run("rm -rf tasks")
        run("cp -r /mnt/github/leLife/tasks tasks")
        # run("chmod 777 celerybeat-schedule")
        run("sudo supervisorctl restart tasks")
