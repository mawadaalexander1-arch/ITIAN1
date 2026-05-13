from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.trainee_list, name='trainee_list'),
    path('<int:trainee_id>/', views.trainee_detail, name='trainee_detail'), 
    path('insert/', views.insert_trainee, name='insert_trainee'),
    path('delete/<int:trainee_id>/', views.hard_delete_trainee, name='hard_delete'),
]
