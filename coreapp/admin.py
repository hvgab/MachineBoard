from django.contrib import admin
from .models import Agent, WeekTarget, MonthTarget, SaleCount

# Register your models here.
@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['nickname']
    list_filter = ['nickname']

@admin.register(WeekTarget)
class WeekTargetAdmin(admin.ModelAdmin):
    list_display = ['agent', 'week', 'target']
    list_filter = ['agent', 'week', 'target']

@admin.register(MonthTarget)
class MonthTargetAdmin(admin.ModelAdmin):
    list_display = ['agent', 'month', 'target']
    list_filter = ['agent', 'month', 'target']

@admin.register(SaleCount)
class SaleCount(admin.ModelAdmin):
    list_display = ['agent', 'date', 'salecount']
    list_filter = ['agent', 'date', 'salecount']
