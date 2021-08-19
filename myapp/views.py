from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,FormView,UpdateView
from django.contrib.auth.views import LoginView,FormView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import SignupForm
from django.contrib import messages

from .models import Task,Project
import datetime


class CustomLogin(LoginView):
    model = Task
    template_name = "login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')

class Signup(CreateView):
    form_class = SignupForm
    #redirect_authenticated_user = True
    template_name = 'signup.html'
    success_url = reverse_lazy('tasks')
    """
    def form_valid(self,form):
        print (form)
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(Signup,self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Signup,self).get(*args,**kwargs)
    """

class TaskList(LoginRequiredMixin,ListView):
    model_project = Project
    model = Task
    template_name = "dashboard.html"
    context_object_name = 'tasks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter().count()
        search_input = self.request.GET.get('inlineRadioOptions') or ""
        if search_input:
            context['tasks'] = context['tasks'].filter(day__icontains=search_input)
        context['search_input'] = search_input
        return context

    def post(self,request):
        model = Task
        if request.method == 'POST':
            key,values= request.POST.items()
            key = values[0]
            model.objects.filter(id = key).update(status=True)
        return redirect('tasks')

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','day','status']
    template_name = "task_form.html"
    success_url = reverse_lazy('tasks')
    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.start_time = (self.request.POST['start_time']).replace('T'," ") + ":00"
        form.instance.end_time = (self.request.POST['end_time']).replace('T'," ") + ":00"
        return super(TaskCreate,self).form_valid(form)
