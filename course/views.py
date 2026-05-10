

# Create your views here.
from django.shortcuts import render, redirect
from .models import Course

def insert_course(request):
    if request.method == 'POST':
        title = request.POST.get('course_name')
        Course.objects.create(title=title)
        return redirect('trainee_list') 
    return render(request, 'course/addcourse.html')

