from fabric.api import *
from fabric.contrib.files import *
import time

#deploy script for QCLOUD
def production():
    env.hosts=['47.52.91.196']
    env.dbhost='127.0.0.1'
    env.dbname='leLife'
    env.dbuser='root'
    env.dbpass='root'
    env.dbport='3306'
    env.dj_setting='production'

def deployweb():
    #deploy web
    with cd("/mnt/github/leLife/web/"):
        run("git pull origin master")
        run("/mnt/envs/env_web/bin/pip3 install -r requirements.txt")
        # run("supervisorctl stop ")
    with settings(warn_only=True):          
        run("sudo pkill uwsgi")        
    with cd("/mnt/deploy_bak"):
        run("rm -rf portal")
        run("cp -r /mnt/deploy/web web")
    with cd("/mnt/deploy"):
        run("rm -rf web")
        run("cp -r /mnt/github/leLife/web web")
    with cd("/mnt/deploy/web"):
        run("python manage.py migrate --noinput --settings=visa.settings.%s" % env.dj_setting)
        # run("python manage.py clearsessions --settings=visa.settings.%s" % env.dj_setting)
        run("python manage.py collectstatic --noinput --settings=visa.settings.%s" % env.dj_setting)
        # run("sudo supervisorctl start 51visa_uwsgi")

def backupdb_dl():
    #db backup
    require('dbhost')
    require('dbname')
    require('dbuser')
    require('dbpass')
    require('dbport')
    require('dj_setting')

    date = time.strftime('%Y%m%d%H%M%S')
    fname = '/tmp/b51visa-%(database)s-backup-%(date)s.gz' % {
        'database': env.dbname,
        'date': date,
    }

    if exists(fname):
        run('rm "%s"' % fname)

    run('mysqldump --default-character-set=utf8mb4 -P %(dbport)s -h %(dbhost)s -u %(username)s -p%(password)s %(database)s  | '
        'gzip > %(fname)s' % {'dbport': env.dbport,
                              'dbhost': env.dbhost,
                              'username': env.dbuser,
                              'password': env.dbpass,
                              'database': env.dbname,
                              'fname': fname})

    get(fname, os.path.basename(fname))
    run('rm "%s"' % fname)


def tcbackupdb_nodl():
    #db backup
    require('dbhost')
    require('dbname')
    require('dbuser')
    require('dbpass')
    require('dbport')
    require('dj_setting')

    date = time.strftime('%Y%m%d%H%M%S')
    fname = '/tmp/b51visa-%(database)s-backup-%(date)s.gz' % {
        'database': env.dbname,
        'date': date,
    }

    if exists(fname):
        run('rm "%s"' % fname)

    run('mysqldump --default-character-set=utf8mb4 -P %(dbport)s -h %(dbhost)s -u %(username)s -p%(password)s %(database)s  | '
        'gzip > %(fname)s' % {'dbport': env.dbport,
                              'dbhost': env.dbhost,
                              'username': env.dbuser,
                              'password': env.dbpass,
                              'database': env.dbname,
                              'fname': fname})

    #keep file on server, do not get backup
    #get(fname, os.path.basename(fname))
    #run('rm "%s"' % fname)

