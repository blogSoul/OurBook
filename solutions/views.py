from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 추가
from .models import Solution
from django.contrib.auth.mixins import LoginRequiredMixin

class SolutionList(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = '/'

    model = Solution
    paginate_by = 10

class SolutionCreate(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = '/'

    model = Solution
    fields = ['title', 'body',]
    success_url = reverse_lazy('s_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

class SolutionDetail(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = '/'
    model = Solution
    count_hit = True 

class SolutionUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = '/'
    model = Solution
    fields = ['title', 'body']
    success_url = reverse_lazy('s_list')

class SolutionDelete(LoginRequiredMixin, DeleteView):
    login_url = '/'
    redirect_field_name = '/'
    model = Solution
    success_url = reverse_lazy('s_list')
