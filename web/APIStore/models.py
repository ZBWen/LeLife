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

'''
    管理 APP KEY
    配置 APP_KEY 使用的API 类型，最大使用次数。
'''
class AppKeySettings(models.Model):
    BJKE = 1

    API_TYPE_CHOICES = (
        (BJKE, u'北京快乐8'),)

    app_key = models.CharField(
                    max_length=32, verbose_name='AppKey')
    api_type = models.IntegerField(
                    choices=API_TYPE_CHOICES, verbose_name='类型')
    create_date = models.DateTimeField(
                    auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(
                    auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = u'配置APP-KEY'
        verbose_name_plural = u'配置APP-KEY'

    def __unicode__(self):
        return self.app_key