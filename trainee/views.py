from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Trainee 
from .forms import TraineeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class TraineeList(LoginRequiredMixin, ListView):
    model = Trainee
    template_name = 'trainee/traineelist.html'
    context_object_name = 'trainees'
    login_url = 'login'

class TraineeDetail(DetailView):
    model = Trainee
    template_name = 'trainee/trainee_detail.html'
    context_object_name = 'trainee'
    pk_url_kwarg = 'trainee_id' 

class TraineeCreate(CreateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/addingTrainee.html'
    success_url = reverse_lazy('trainee_list')

class TraineeDelete(DeleteView):
    model = Trainee
    pk_url_kwarg = 'trainee_id'
    success_url = reverse_lazy('trainee_list')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login') 