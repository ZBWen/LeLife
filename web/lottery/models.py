from django.db import models

class BJkeNo(models.Model):
    issue = models.CharField(max_length=16, verbose_name='期号')
    nums = models.CharField(max_length=128, verbose_name='开奖号码')
    frisbee = models.IntegerField(verbose_name='飞盘')
    pc_nums = models.CharField(max_length=23, verbose_name='PC28号码')
    pc_sum = models.IntegerField(verbose_name='PC28值')
    date = models.DateTimeField(verbose_name='开奖时间')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='获取时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '北京快乐8'
        verbose_name_plural = '北京快乐8'
        ordering = ['-issue']


class LotteryMiss(models.Model):
    KBKE = 8601001

    LOTTERY_TYPE_CHOICES = (
                    (KBKE,'北京快乐8'),
    )

    lottery_type = models.IntegerField(choices=LOTTERY_TYPE_CHOICES, verbose_name='类型')
    issue = models.CharField(max_length=16, verbose_name='期号')
    is_insert = models.BooleanField(default=False, verbose_name='插入')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '开奖遗漏期'
        verbose_name_plural = '开奖遗漏期'
        ordering = ['lottery_type','-issue']