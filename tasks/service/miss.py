# -*- coding: utf-8 -*-
import time
import datetime
import traceback

from tasks.utils.redis import redis_connt
from tasks.utils.mysql import Mysql

# 北京快乐8
KBKE = 8601001

class Prevkeno(object):

    def get_miss_prevkeno():
        SELECT_SQL = '''
                SELECT 
                    issue 
                FROM 
                    lottery_lotterymiss 
                WHERE is_insert=0;
            '''
        mysql = Mysql()
        result = mysql.getMany(SELECT_SQL,300)
        print (result)
        return result

    def select_miss(self,issue_len=1000):
        issue = 0  # 期号，期号计数
        first_issue = int(redis_connt.get('MISS_PREVKENO_FIRST',default=0))
        res_issue = first_issue # 循环到期号， 已存在的期号

        mysql = Mysql()
        if not first_issue:
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
               first_issue = int(result['issue'])

        SELECT_SQL = '''
                SELECT 
                    issue 
                FROM 
                    lottery_bjkeno 
                WHERE issue>{}
                ORDER BY issue;
            '''.format(first_issue)
        result = mysql.getMany(SELECT_SQL,issue_len)
        try:
            for info in result:
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

                res_issue = int(info['issue'])
                issue = int(info['issue']) if not issue else issue+1
                if issue == res_issue:
                    continue
                else:
                    print ('{}-{}'.format(issue,res_issue))
                    for i in range(res_issue-issue):
                        SQL = '''
                            INSERT INTO 
                                lottery_lotterymiss (lottery_type,issue,is_insert,create_date,update_date) 
                            VALUES ('{}','{}','{}','{}','{}');
                            '''.format(KBKE,issue+i,0,datetime.datetime.now(),datetime.datetime.now())
                        mysql.insertOne(SQL)
                    issue = res_issue
            mysql.dispose()
            redis_connt.set('MISS_PREVKENO_FIRST',res_issue)
        except Exception as e:
            print ('e %s' % traceback.format_exc())
            mysql.dispose(isEnd=0)
