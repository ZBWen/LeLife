# -*- coding: utf-8 -*-
import time
import datetime

from tasks.utils.redis import redis_connt
from tasks.utils.mysql import Mysql

# 北京快乐8
KBKE = 8601001

class Prevkeno(object):

    def select_miss(self):
        issue = 0
        res_issue = 0
        last_issue = int(redis_connt.get('NEW_PREVKENO',default=0))
        mysql = Mysql()
        MISS_SQL = '''
                SELECT 
                    issue 
                FROM 
                    lottery_lotterymiss 
                WHERE lottery_type={} 
                ORDER BY -issue;
            '''.format(KBKE)
        result = mysql.getOne(MISS_SQL)
        if result:
           issue = int(result['issue'])

        SELECT_SQL = '''
                SELECT 
                    issue 
                FROM 
                    lottery_bjkeno 
                WHERE issue>{}
                ORDER BY issue;
            '''.format(issue)
        print (SELECT_SQL)
        result = mysql.getAll(SELECT_SQL)
        print (len(result))
        try:
            for info in result[:1000]:
                if not issue:
                    issue = int(info['issue'])
                if res_issue == int(info['issue']):
                    print ('delete:{}'.format(res_issue))
                    # 删除重复的数据
                    DELETE_SQL = '''
                        DELETE 
                            FROM 
                                lottery_bjkeno 
                            WHERE 
                                issue={} AND id NOT IN (
                                    SELECT id from (
                                        SELECT id 
                                            FROM 
                                                lottery_bjkeno a
                                            WHERE issue={} 
                                            HAVING MIN(id)
                                        ) a
                                    );
                        '''.format(res_issue,res_issue)
                    mysql.delete(DELETE_SQL)
                    continue
                issue += 1
                res_issue = int(info['issue'])
                if issue == res_issue:
                    continue
                else:
                    print ('{}-{}'.format(res_issue,issue))
                    for i in range(res_issue-issue):
                        SQL = '''
                            INSERT INTO 
                                lottery_lotterymiss (lottery_type,issue,is_insert,create_date,update_date) 
                            VALUES ('{}','{}','{}','{}','{}');
                            '''.format(KBKE,issue+i,0,datetime.datetime.now(),datetime.datetime.now())
                        mysql.insertOne(SQL)
                    issue = res_issue
            mysql.dispose()
        except Exception as e:
            print ('e %s' % e)
            mysql.dispose(isEnd=0)
