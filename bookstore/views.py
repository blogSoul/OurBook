from django.shortcuts import render, redirect
import urllib.request
import json
from django.urls import reverse_lazy

from django.utils import timezone
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 추가
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

################ Book Product CRUD ############################################3

class BookList(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = '/'

    model = Product
    paginate_by = 10

class BookCreate(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = '/'

    model = Product
    fields = ['book', 'note', 'ex_type', 'state', 'exc_method']
    success_url = reverse_lazy('book_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

class BookDetail(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = '/'
    model = Product

class BookUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = '/'
    model = Product
    fields = ['book', 'note', 'ex_type', 'state', 'exc_method']
    success_url = reverse_lazy('book_list')

class BookDelete(LoginRequiredMixin, DeleteView):
    login_url = '/'
    redirect_field_name = '/'
    model = Product
    success_url = reverse_lazy('book_list')

#############################################################3

def books(request):

    if request.method == 'POST':
        
        keyword = request.POST.get('book_search', '') # form의 이름이 quote였으니까.
        client_id = "CJNbcDFvgOnPbjtdXxA_"  # Client-Id
        client_secret = "6EdIJ7Pe2d"        # Client-Secret
        encText = urllib.parse.quote(keyword)
        
        url = "https://openapi.naver.com/v1/search/book?query=" + encText +"&display=3&sort=count" # 우선은 3씩, 판매량 순
        request_content = urllib.request.Request(url)
        
        request_content.add_header("X-Naver-Client-Id", client_id)
        request_content.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request_content)
        rescode = response.getcode()
        
        if(rescode==200):
            response_body = response.read()
            # print(response_body.decode('utf-8'))

            json_rt = response_body.decode('utf-8')
            final_res = json.loads(json_rt)
            return render(request, 'books.html', {'final_res':final_res})
        
        else:
            # print("Error Code:" + rescode)
            final_res = rescode

        final_res = final_res.decode('utf-8')

        return render(request, 'books.html', {'final_res':final_res})


    # 페이지로 들어온 경우
    else:
        return render(request, 'book_list.html', {}) 

    return render(request, 'book_list.html')

def new_book(request):

    return render(request, 'save_book.html')