from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('upload_image/', views.addImage),
    path('compare_faces/', views.compareFaces),

]
