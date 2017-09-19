from django.db import models

class BJkeNo(models.Model):
    issue = models.CharField(max_length=16, verbose_name='期号')
    nums = models.CharField(max_length=128, verbose_name='开奖号码')
    frisbee = models.IntegerField(verbose_name='飞盘')
    pc_nums = models.CharField(max_length=23, verbose_name='PC28号码')
    pc_sum = models.IntegerField(verbose_name='PC28值')
    date = models.DateTimeField(verbose_name='开奖时间')
    create_date = models.DateTimeField(verbose_name='获取时间')

    class Meta:
        verbose_name = '北京快乐8'
        verbose_name_plural = '北京快乐8'
        ordering = ['-issue']