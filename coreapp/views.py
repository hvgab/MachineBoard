from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.utils import timezone
import datetime as dt
from .models import SaleCount, Agent
from .forms import ActivateForm
# Create your views here.

class Home(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return SaleCount.objects.all().filter(date=dt.date.today())

class AgentList(ListView):
    model = Agent
    form = ActivateForm()

class SaleCountCreate(CreateView):
    model = SaleCount
    fields = ['agent', 'date', 'salecount']

def activate_agent(request):
    if request.method == 'POST':
        next = request.POST.get('next', 'home')
        agent = Agent.objects.get(id=request.POST['agent_id'])
        sc = SaleCount(agent=agent, date=timezone.now(), salecount=0)
        sc.save()
        return redirect(next)
    return redirect('home')

def change_salecount(request):
    if request.method == 'POST':
        next = request.POST.get('next', 'home')
        updown = request.POST.get('updown')
        sc = SaleCount.objects.get(id=request.POST['sc_id'])
        if updown == 'down':
            sc.salecount -= 1
        else:
            sc.salecount += 1
        sc.save()
        return redirect(next)
    return redirect('home')

def increment_salecount(request):
    if request.method == 'POST':
        next = request.POST.get('next', 'home')
        sc = SaleCount.objects.get(id=request.POST['sc_id'])
        sc.salecount += 1
        sc.save()
        return redirect(next)
    return redirect('home')

def decrement_salecount(request):
    if request.method == 'POST':
        next = request.POST.get('next', 'home')
        # agent = Agent.objects.get(id=request.POST['agent_id'])
        # sc = SaleCount.objects.filter(SaleCount.date==dt.date.today(), agent==agent).first()
        sc = SaleCount.objects.get(id=request.POST['sc_id'])
        sc.salecount -= 1
        sc.save()
        return redirect(next)
    return redirect('home')
