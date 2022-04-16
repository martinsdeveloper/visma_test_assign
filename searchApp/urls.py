from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_records, name='search_records'),
    path('delete/<int:id>/', views.delete_search, name='delete_search'),
    path('change_language/<locale>/', views.change_language, name='change_language'),
]
