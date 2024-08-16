from django.urls import path

from app import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('thanks/', views.thanks_view, name='thanks'),
]