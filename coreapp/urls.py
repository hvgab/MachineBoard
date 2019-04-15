from django.urls import path
from .views import *

name = 'mb'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('agents/', AgentList.as_view(), name='agent-list'),
    # path('salecounts/', SaleCountList.as_view()),
    path('salecounts/create', SaleCountCreate.as_view(), name='salecount-create'),

    path('sc/activate/', activate_agent, name='sc-activate'),
    path('sc/increment/', increment_salecount, name='sc-increment'),
    path('sc/decrement/', decrement_salecount, name='sc-decrement'),
    path('sc/change/', change_salecount, name='sc-change'),
]
