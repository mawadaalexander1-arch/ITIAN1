from django.shortcuts import render, redirect
from .models import Trainee 

def trainee_list(request):
    trainees = Trainee.objects.all() 
    return render(request, 'trainee/traineelist.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Trainee.objects.create(name=name, email=email)
        return redirect('trainee_list')
    
    return render(request, 'trainee/add_trainee.html')

def delete_trainee(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)
    trainee.delete()
    return redirect('trainee_list')