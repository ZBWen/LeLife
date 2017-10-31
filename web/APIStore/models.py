import uuid

from django.db import models

'''
	管理API商城KEY
	一个GUID 为一个用户不可重复，同一个GUID 可以有多个APP_KEY
	每一个 app_key 对应一个用户的api类型，原则上不允许重复
'''
class APIStoreKeys(models.Model):
	guid = models.CharField(max_length=36,
					default=uuid.uuid1(), verbose_name='AppKey')
	app_key = models.CharField(
					max_length=32, verbose_name='AppKey')
	create_date = models.DateTimeField(
					auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(
    				auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = u'API商城KEY'
        verbose_name_plural = u'API商城KEY'

    def __unicode__(self):
        return self.guid