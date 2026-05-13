from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TraineeList.as_view(), name='trainee_list'),
    path('<int:trainee_id>/', views.TraineeDetail.as_view(), name='trainee_detail'),
    path('insert/', views.TraineeCreate.as_view(), name='insert_trainee'),
    path('delete/<int:trainee_id>/', views.TraineeDelete.as_view(), name='hard_delete'),
]