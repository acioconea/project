from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from companies.models import Companies


class CompaniesView(ListView):

    model = Companies
    template_name = 'companies/company_index.html'




class CreateCompanyView(LoginRequiredMixin, CreateView):

    model = Companies
    fields = ['name', 'website','company_type','location']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


class UpdateCompanyView(LoginRequiredMixin,UpdateView):
    model = Companies
    fields = ['name', 'website','company_type','location']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


@login_required
def deactivate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=False)
    return redirect('companies:lista_companii')

@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=True)
    return redirect('companies:lista_companii')