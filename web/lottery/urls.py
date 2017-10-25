
from django.conf.urls import include, url

from lottery.views import *

urlpatterns =(
    url(r'^show/keno/$', ShowKenoView.as_view(),name='show_keno'),
    )

    