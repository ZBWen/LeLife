from django.contrib import admin

from lottery.models import *

class BJkeNoAdmin(admin.ModelAdmin):
    search_fields = ('issue',)
    list_display = (
        'issue', 'nums', 'frisbee', 'pc_nums', 'pc_sum', 'date',
        'create_date'
    )


admin.site.register(BJkeNo, BJkeNoAdmin)