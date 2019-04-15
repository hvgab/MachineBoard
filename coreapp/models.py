from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import calendar
# Create your models here.
class Agent(models.Model):
    nickname = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nickname

class WeekTarget(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    week = models.IntegerField()
    target = models.IntegerField()
    def __str__(self):
        return f'{self.agent.nickname} W.{self.week} = {self.target}'

class MonthTarget(models.Model):
    MONTH_CHOICES = tuple((m, m) for m in calendar.month_name[1:])
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    month = models.CharField(max_length=15, choices=MONTH_CHOICES)
    target = models.IntegerField()
    def __str__(self):
        return f'{self.agent.nickname} M.{self.month} = {self.target}'

class SaleCount(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    salecount = models.IntegerField()

    class Meta:
        unique_together = ('agent', 'date')

    def __str__(self):
        return f'{self.agent.nickname} {self.date} = {self.salecount}'
