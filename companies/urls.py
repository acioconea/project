from django.urls import path

from companies import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompanyView.as_view(), name='adaugare'),
    path('<int:pk>/modificare/', views.UpdateCompanyView.as_view(), name='modifica'),
    path('<int:pk>/dezactiveaza/', views.deactivate_company, name='dezactiveaza'),
    path('<int:pk>/activeaza/', views.activate_company, name='activeaza'),
]