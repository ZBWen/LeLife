from django.contrib import admin

from lottery.models import *

class BJkeNoAdmin(admin.ModelAdmin):
    search_fields = ('issue',)
    list_display = (
        'issue', 'nums', 'frisbee', 'pc_nums', 'pc_sum', 'date',
        'create_date'
    )

class LotteryMissAdmin(admin.ModelAdmin):
    search_fields = ('issue',)
    list_display = (
        'lottery_type', 'issue','update_date', 'create_date', 'is_insert'
    )
    list_filter = ('lottery_type','is_insert')
  
admin.site.register(BJkeNo, BJkeNoAdmin)
admin.site.register(LotteryMiss, LotteryMissAdmin)