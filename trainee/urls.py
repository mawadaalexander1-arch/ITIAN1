from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.trainee_list, name='trainee_list'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('delete/<int:trainee_id>/', views.delete_trainee, name='delete_trainee')
]