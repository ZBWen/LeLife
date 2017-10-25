from django.shortcuts import render

from django.views.generic import TemplateView

from lottery.models import *

class ShowKenoView(TemplateView):
    template_name = 'keno/keno.html'

    def get(self, request, *args, **kwargs):
      
        return super(ShowKenoView,self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(ShowKenoView,self).get_context_data(**kwargs)
       
        return context_data